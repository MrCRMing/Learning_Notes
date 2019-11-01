import pickle
import numpy as np
import copy


class AdaBoostClassifier:
    '''A simple AdaBoost Classifier.'''

    def __init__(self, weak_classifier, n_weakers_limit):
        '''Initialize AdaBoostClassifier

        Args:
            weak_classifier: The class of weak classifier, which is recommend to be sklearn.tree.DecisionTreeClassifier.
            n_weakers_limit: The maximum number of weak classifier the model can use.
        '''
        self.weak_classifier = weak_classifier
        self.n_weakers_limit = n_weakers_limit
        self.classifier_list = []
        for i in range(self.n_weakers_limit):
            new_weak_classifier=copy.deepcopy(self.weak_classifier)
            self.classifier_list.append(new_weak_classifier)
        self.alpha_list = []  # used for the weight of the voting

    def is_good_enough(self):
        '''Optional'''
        pass

    def fit(self, X, y):
        '''Build a boosted classifier from the training set (X, y).

        Args:
            X: An ndarray indicating the samples to be trained, which shape should be (n_samples,n_features).
            y: An ndarray indicating the ground-truth labels correspond to X, which shape should be (n_samples,1).
        '''

        sample_weight=(np.ones(X.shape[0])*(1.0/X.shape[0]))

        for i in range(self.n_weakers_limit):
            classifier=self.classifier_list[i]
            classifier.fit(X,y,sample_weight)
            y_predict=classifier.predict(X)
            index=0
            error=0
            for y_pre,y_label in zip(y_predict,y):
                if y_pre!=y_label:
                    error+=sample_weight[index]*1
                index+=1
            if error==0:
                error=0.0000000000000000001
            if error>0.5:
                print("error rate>0.5,please try to train again")
                break

            alpha=1/2*np.log((1-error)/error)
            self.alpha_list.append(alpha)
            sample_weight_temp=sample_weight*np.exp(-1*alpha*y_predict*y)
            sample_weight=sample_weight_temp/sum(sample_weight_temp)


    def predict_scores(self, X):
        '''Calculate the weighted sum score of the whole base classifiers for given samples.

        Args:
            X: An ndarray indicating the samples to be predicted, which shape should be (n_samples,n_features).

        Returns:
            An one-dimension ndarray indicating the scores of differnt samples, which shape should be (n_samples,1).
        '''
        pre_scores=np.zeros(X.shape[0])
        for i in range(self.n_weakers_limit):
            pre_scores+=self.alpha_list[i]*self.classifier_list[i].predict(X)

        return pre_scores

    def predict(self, X, threshold=0):
        '''Predict the catagories for geven samples.

        Args:
            X: An ndarray indicating the samples to be predicted, which shape should be (n_samples,n_features).
            threshold: The demarcation number of deviding the samples into two parts.

        Returns:
            An ndarray consists of predicted labels, which shape should be (n_samples,1).
        '''
        pre_scores=self.predict_scores(X)
        pre_label=np.zeros(X.shape[0])
        for i in range(X.shape[0]):
            if pre_scores[i]>0:
                pre_label[i]=1
            else:
                pre_label[i]=-1

        return pre_label

    @staticmethod
    def save(model, filename):
        with open(filename, "wb") as f:
            pickle.dump(model, f)

    @staticmethod
    def load(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
