# coding=utf-8

import numpy as np
# myfile = open(r'C:\Users\Administrator\.spyder\00ll\2016.09.10\simple_matplotloib\IrisData.txt','r')
# datasets = myfile.read()
# numberOfLines = len(myfile.readlines())




# def file2matrix(myfile):
#     myfile = open(r'C:\Users\Administrator\.spyder\00ll\2016.09.10\simple_matplotloib\IrisData.txt','r')
#     numberOfLines = len(myfile.readlines())         #get the number of lines in the file
#     returnMat = zeros((numberOfLines,30))        #prepare matrix to return
#     classLabelVector = []                       #prepare labels return
#
#     index = 0
#     for line in myfile.readlines():
#         line = line.strip()
#         # listFromLine = line.split('\t')
#         returnMat[index,:] = line[0:3]
#         classLabelVector.append(line[-1])
#         index += 1
#     return returnMat,classLabelVector



import sklearn.datasets
import sklearn.linear_model
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
import sys

# myfile = open(r'C:\Users\Administrator\.spyder\00ll\2016.09.10\simple_matplotloib\IrisData.txt','r')
# datasets = myfile.read()
# a = datasets.split('\t')
#
# def splist(l,s):
#     return [l[i:i+s] for i in range(len(l)) if i%s==0]
#
# b = splist(datasets,5)
#
# print datasets


#生成数据集并绘制它
np.random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.20)
# X, y = returnMat([:]) ,classLabelVector
plt.scatter(X[:, 0], X[:, 1], s=40, c=y, cmap=plt.cm.Spectral)
plt.scatter(X[:, 0], X[:, 1], s=40, c=y, cmap=plt.cm.Spectral)
# －－－－－－－－－－－－－－－－－－－－－－－－－－－
#---------------------------------------------------
# BP
# 定义梯度下降一些有用的变量和参数
num_examples = len(X)  # 训练集大小
nn_input_dim = 2  # 输入层维度
nn_output_dim = 2  # 输出层维度
# 梯度下降参数 (我手动选择)
epsilon = 0.01  # 梯度下降的学习率
reg_lambda = 0.01  # 正则化程度


class tempmodel():
    model = {}

    # 辅助功能，评价数据集上总损失
    def calculate_loss(self):
        W1, b1, W2, b2 = self.model['W1'], self.model['b1'], self.model['W2'], self.model['b2']
        # 正向传播，计算预测值。
        z1 = X.dot(W1) + b1
        a1 = np.tanh(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        # 计算损失
        corect_logprobs = -np.log(probs[range(num_examples), y])
        data_loss = np.sum(corect_logprobs)
        # 给损失添加正则化项 Add regulatization term to loss (optional)
        data_loss += reg_lambda / 2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
        return 1. / num_examples * data_loss
        # 辅助函数，预测输出（0或1） to predict an output (0 or 1)
#---------------------------
    def predict(self, X):  # 这个‘X’大小写都无所谓，因为，predict是函数plot_decision_regions自己调用的，会自动以第一个函数传入给‘X’
        W1, b1, W2, b2 = self.model['W1'], self.model['b1'], self.model['W2'], self.model['b2']
        # 向前传播
        z1 = X.dot(W1) + b1
        a1 = np.tanh(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        return np.argmax(probs, axis=1)
        # 这个函数学习神经网络的参数，并返回模型 。

    # - nn_hdim: 隐层结点数
    # - num_passes: Number of passes through the training data for 梯度下降。
    # - print_loss: If True, 每迭代 1000 ，打印损失。
    def build_model(self, nn_hdim, num_passes=20000, print_loss=False):
        # 参数初始化为随机值. We need to learn these.
        np.random.seed(0)
        W1 = np.random.randn(nn_input_dim, nn_hdim) / np.sqrt(nn_input_dim)
        b1 = np.zeros((1, nn_hdim))
        W2 = np.random.randn(nn_hdim, nn_output_dim) / np.sqrt(nn_hdim)
        b2 = np.zeros((1, nn_output_dim))
        # 这是我们想最终返回的值
        model = {}
#-----------------------------

        # 梯度下降，对每一批量...
        for i in xrange(0, num_passes):
            # 向前传播
            z1 = X.dot(W1) + b1
            a1 = np.tanh(z1)
            z2 = a1.dot(W2) + b2
            exp_scores = np.exp(z2)
            probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
            # 向后传播
            delta3 = probs
            delta3[range(num_examples), y] -= 1
            dW2 = (a1.T).dot(delta3)
            db2 = np.sum(delta3, axis=0, keepdims=True)
            delta2 = delta3.dot(W2.T) * (1 - np.power(a1, 2))
            dW1 = np.dot(X.T, delta2)
            db1 = np.sum(delta2, axis=0)
            # 增加正则化项 (b1 and b2 没有正则化项)
            dW2 += reg_lambda * W2
            dW1 += reg_lambda * W1
            # 梯度下降参数更新
            W1 += -epsilon * dW1
            b1 += -epsilon * db1
            W2 += -epsilon * dW2
            b2 += -epsilon * db2
            # 为模型分配新参数
            self.model = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}
            # Optionally 打印损失.
            # 它使用整个数据集,因此它是昂贵的。 so we don't want to do it too often.
            if print_loss and i % 1000 == 0:
                print "Loss after iteration %i: %f" % (i, self.calculate_loss())


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            degree = 4
        else:
            degree = int(sys.argv[1])
    except:
        print "usage:python 2BP.py degree(a number,default equal to 3)"
        sys.exit(0)

    rmodel = tempmodel()
    # 建一个3维度隐层的模型
    rmodel.build_model(degree, print_loss=True)
    # 画出决策边界
    plot_decision_regions(X, y, rmodel, legend=0)  # 必须改成类模式，因为这个函数要求传入的对象有predict函数
    plt.title("Decision Boundary for hidden layer size %d" % degree)
    plt.show()