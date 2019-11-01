import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_columns = None
pd.options.display.max_rows = None

train_data = pd.read_csv('TrainSet.csv')
test_data = pd.read_csv('TestSet.csv')

# 用平均值填补空缺值
for column in list(train_data.columns[train_data.isnull().sum() > 0]):
    mean_val = train_data[column].mean()
    train_data[column].fillna(mean_val, inplace=True)

for column in list(test_data.columns[test_data.isnull().sum() > 0]):
    mean_val = test_data[column].mean()
    test_data[column].fillna(mean_val, inplace=True)

# print(train_data.describe())
# print(test_data.describe())

# 划分数据
# 在样本数据插入一列“1”，为了得到偏置
if 'Ones' not in train_data.columns:
    train_data.insert(0, 'Ones', 1)
if 'Ones' not in test_data.columns:
    test_data.insert(0, 'Ones', 1)

train_X = train_data.iloc[:, :-2].values
train_y = train_data.iloc[:, -2].values
test_X = test_data.iloc[:, :-2].values
test_y = test_data.iloc[:, -2].values

theta = np.zeros(train_X.shape[1])
print(train_X.shape, theta.shape)


# 定义拟合函数
def f(theta, X):
    y = X @ theta
    return y


# 定义代价函数
def loss(theta, X, y):
    m = X.shape[0]
    loss = 1 / (2 * m) * sum(np.power((f(theta, X) - y), 2))
    return loss


# 梯度下降
def gradientDescent(X, y, theta, alpha, epoch=1000):
    cost = np.zeros(epoch)  # 初始化一个cost列表 用于保存每次的cost值
    m = X.shape[0]

    for i in range(epoch):
        cost[i] = loss(theta, X, y)
        temp = theta - (alpha / m) * (X.T @ (f(theta, X) - y))
        theta = temp

    return theta, cost


epoch = 15
new_theta, new_cost = gradientDescent(train_X, train_y, theta, alpha=0.00001, epoch=epoch)
# print(sum(np.power((train_y - f(theta, train_X)),2)))

# 画出学习曲线
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(np.arange(epoch), new_cost, 'r')
ax.set_xlabel('Interations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')
plt.show()

# 在验证集验证模型泛化能力
new_loss=loss(new_theta,test_X,test_y)
print(new_loss)
