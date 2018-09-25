#encoding:utf-8
from numpy import *
#和import Numpy的区别是，引用函数名更方便，可直接引用函数名。
import matplotlib.pyplot as plt
import operator
#operator模块是python中内置的操作符函数接口，它定义了一些算术和比较内置操作的函数。
#operator模块是用c实现的，所以执行速度比python代码快。
import time

#定义创建数据集，返回训练数据和标签
def createTrainDataSet():#训练样本,第一个1为阈值对应的w，下同
    trainData=[   [1, 1, 4],
                    [1, 2, 3],
                    [1, -2, 3],
                    [1, -2, 2],
                    [1, 0, 1],
                    [1, 1, 2]]
    label=[1, 1, 1, -1, -1,  -1]
    #○为-1，□为+1
    return trainData, label
def createTestDataSet():#数据样本
    testData = [   [1, 1, 1],
                   [1, 2, 0],
                   [1, 2, 4],
                   [1, 1, 3]]
    return testData
def sigmoid(X):
    X=float(X)
    if X>0:
        return 1
    elif X<0:
        return -1
    else:
        return 0
def pla(traindataIn,trainlabelIn):
    traindata=mat(traindataIn)
    trainlabel=mat(trainlabelIn).transpose()
    m,n=shape(traindata)
    w=ones((n,1))
    while True:
        iscompleted=True
        for i in range(m):
            if (sigmoid(dot(traindata[i],w))==trainlabel[i]):
                continue
            else:
                iscompleted=False
                w+=(trainlabel[i]*traindata[i]).transpose()
        if iscompleted:
            break
    return w
def classify(inX,w):
    result=sigmoid(sum(w*inX))
    if result>0:
        return 1
    else:
        return -1
def plotBestFit(w):
    traindata,label=createTrainDataSet()
    dataArr = array(traindata)
    n = shape(dataArr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        if int(label[i])==1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig=plt.figure()
    ax= fig.add_subplot(111)
    ax.scatter(xcord1, ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2, ycord2,s=30,c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-w[0]-w[1] * x)/w[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()
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