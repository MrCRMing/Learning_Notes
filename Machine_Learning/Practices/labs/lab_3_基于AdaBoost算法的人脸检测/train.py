from PIL import Image
import os
import pickle
import feature
import numpy as np
import random
import pandas as pd
from ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report

def get_path(path):
    """
    返回目录中所有jpg图像的文件名图片
    """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def preprocess_data():
    """
    预处理数据
    :return:
    """
    # 判断预处理数据文件是否存在，若不存在则执行预处理
    if not os.path.exists('NPD_feature.pkl'):
        # 获得所有图片路径名
        d = os.path.dirname(__file__)
        face_img_path_list = get_path(d + '/datasets/original/face')
        nonface_img_path_list = get_path(d + '/datasets/original/nonface')
        img_path_list = face_img_path_list + nonface_img_path_list
        # 构建标签
        face_label = np.ones(len(face_img_path_list)).astype(int)
        nonface_label = np.ones(len(nonface_img_path_list)).astype(int) * -1
        label = np.insert(nonface_label, 0, values=face_label, axis=0)

        # 将图片路径和标签同步打乱，构成随机数据集
        temp = list(zip(img_path_list, label))
        random.shuffle(temp)
        img_path_list[:], label[:] = zip(*temp)

        NPD_feature_list = []
        # 读取图片，将全部图片转成大小为24*24的灰度图
        # 提取NPD特征，并通过dump()函数将预处理后的特征数据保存起来
        for img_item in img_path_list:
            img = Image.open(img_item).convert('L')
            img = img.resize((24, 24), Image.ANTIALIAS)
            # 转换成np.ndarray格式
            img = np.array(img)
            NPDFeature_obj = feature.NPDFeature(img)
            NPD_feature = NPDFeature_obj.extract()

            NPD_feature_list.append(NPD_feature)

        # 序列化特征列表，存储在文件中，方便下次调用
        with open('NPD_feature.pkl', 'wb') as f:
            pickle.dump(NPD_feature_list, f)

        # 将标签保存起来
        data = pd.DataFrame({'label': label})
        data.to_csv('label.csv')

    else:
        print("preprocessing has been performed")


if __name__ == "__main__":
    # 预处理数据
    preprocess_data()
    # 加载数据
    feature = AdaBoostClassifier.load('NPD_feature.pkl')
    label = pd.read_csv('label.csv')['label']
    feature = np.array(feature)
    label = np.array(label)

    # 划分训练集和验证集
    X_train, X_val, y_train, y_val = train_test_split(feature, label, test_size=0.4, random_state=2019, shuffle=True)
    print('X_train.shape', X_train.shape)
    print('X_val.shape', X_val.shape)
    print('y_train.shape', y_train.shape)
    print('y_val.shape', y_val.shape)

    # 尝试使用不同深度的决策树，不同数量的决策树来进行建模和预测
    result = []
    max_depth = 4
    max_num_tree = 10
    for depth in range(1, max_depth + 1):
        result_item = []
        for num_tree in range(1, max_num_tree + 1):
            adaboostclassifier = AdaBoostClassifier(DecisionTreeClassifier(max_depth=depth), num_tree)
            adaboostclassifier.fit(X_train, y_train)
            pre_label = adaboostclassifier.predict(X_val)
            correct = [1 if a == b else 0 for (a, b) in zip(pre_label, y_val)]
            accurary = sum(correct) / len(correct)
            result_item.append(accurary * 100)

            report=classification_report(y_val,pre_label,labels=[-1,1],target_names=["face","nonface"])
            model_num=(depth-1)*10+num_tree
            with open('report.txt', 'a') as f:
                    f.write('\nmodel '+str(model_num)+':\n')
                    f.write('number of decision tree:'+str(num_tree)+'\n')
                    f.write('max_depth of decision tree:' + str(depth) + '\n')
                    f.write(report)
            print("model "+str(model_num)+"/40 is finished")
        result.append(result_item)
    # 画出模型预测情况

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(np.arange(1, max_num_tree + 1), result[0], 'red', label='tree_depth=1')
    ax.plot(np.arange(1, max_num_tree + 1), result[1], 'green', label='tree_depth=2')
    ax.plot(np.arange(1, max_num_tree + 1), result[2], 'blue', label='tree_depth=3')
    ax.plot(np.arange(1, max_num_tree + 1), result[3], 'black', label='tree_depth=4')

    plt.legend()
    ax.set_xlabel('num of decision tree')
    ax.set_ylabel('accurary/%')
    ax.set_title('Model performance comparison')
    plt.show()
