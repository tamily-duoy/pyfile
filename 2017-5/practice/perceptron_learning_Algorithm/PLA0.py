#encoding:utf-8
from numpy import *
#和import Numpy的区别是，引用函数名更方便，可直接引用函数名。
import matplotlib.pyplot as plt
import operator
#operator模块是python中内置的操作符函数接口，它定义了一些算术和比较内置操作的函数。
#operator模块是用c实现的，所以执行速度比python代码快。
import time

#定义---创建数据集，返回训练数据和标签--------------------------
def createTrainDataSet():#训练样本，下同
    trainData=[   [1, 1, 4],
                [1, 2, 3],
                [1, -2, 3],
                [1, -2, 2],
                [1, 0, 1],
                [1, 1, 2]]
    label=[1, 1, 1, -1, -1,  -1]
    #○为-1，□为+1
    return trainData, label
#定义---创建测试集，返回测试数据---目的，预测标签------------------
def createTestDataSet():#数据样本
    testData = [   [1, 1, 1],
                   [1, 2, 0],
                   [1, 2, 4],
                   [1, 1, 3]]
    return testData
#定义---标签的分类函数，返回分类的类别----目的，根据标准，预测分类--------
#                   当X为正时，预测为正类；当X为负时，预测为负类。-------
def sigmoid(X):
    X=float(X)   #把X强制转换为浮点数
    if X>0:
        return 1
    elif X<0:
        return -1
    else:
        return 0

#定义PLA的输入数据和标签---返回权值--------------------------------
#                 将数据集list强制转化为矩阵
def pla(traindataIn,trainlabelIn):
    traindata=mat(traindataIn)
    trainlabel=mat(trainlabelIn).transpose()
    m,n=shape(traindata)
    w=ones((n,1))
    while True:
        iscompleted=True
        for i in range(m):
            if (sigmoid(dot(traindata[i],w))==trainlabel[i]):        #dot为坐标
                continue
            else:
                iscompleted=False
                w+=(trainlabel[i]*traindata[i]).transpose()
        if iscompleted:
            break
    return w
#定义分类： +1类和-1类
def classify(inX,w):
    #分类函数：sigmoid函数
    result=sigmoid(sum(w*inX))
    if result>0:
        return 1
    else:
        return -1
#定义可视化函数
def plotBestFit(w):
    traindata,label=createTrainDataSet()    #训练集
    dataArr = array(traindata)              #测试集
    n = shape(dataArr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
#图上两类点的位置排放
    for i in range(n):
        if int(label[i])==1:                # +1 类的位置
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:                              # -1 类的位置
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig=plt.figure()                        #画图
    ax= fig.add_subplot(111)                #图纸位置
    ax.scatter(xcord1, ycord1,s=30,c='red',marker='s')     #图样
    ax.scatter(xcord2, ycord2,s=30,c='green')
    x = arange(-3.0, 3.0, 0.1)               #横坐标范围
    y = (-w[0]-w[1] * x)/w[2]                #纵坐标的值
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()

#定义分类（数据集，权值）
def classifyall(datatest,w):
    predict=[]
    for data in datatest:
        result=classify(data,w)
        predict.append(result)
    return predict
def main():
    trainData,label=createTrainDataSet()
    testdata=createTestDataSet()
    w=pla(trainData,label)
    result=classifyall(testdata,w)
    plotBestFit(w)
    print (w)
    print (result)
if __name__=='__main__':
    start = time.clock()
    main()
    end = time.clock()
    print('finish all in %s' % str(end - start))