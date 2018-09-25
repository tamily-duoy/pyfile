#encoding:utf-8
#从sklearn载入数据集，确定维度和噪声
from numpy import *
import sklearn
import sklearn.datasets
import matplotlib.pyplot as plt
import matplotlib
import operator
import sklearn.linear_model
import time
def createData(dim=200,cnoise=0.2):
    random.seed(0)                                   #与上次随机数相同
    X,y=sklearn.datasets.make_moons(dim,noise=cnoise)#创造二分类的数据集
    #plt.scatter(X[:,0],X[:,1],s=40,c=y,cmap=plt.cm.Spectral)#cmap里面的参数为一种布局方式，y在此处既代表点的种类，也代表点的颜色，http://matplotlib.org/api/colors_api.html
    num=len(y)
    x_change=ones((200,1))
    X=hstack((x_change,X))   #合并为数组array
    for i in range(num):
        if y[i]==0:
            y[i]=-1
    return X,y
#定义分类标准函数
def sigmoid(X):
    X = float(X)
    if X>0:
        return 1
    elif X<0:
        return -1
    else:
        return 0
#定义分类（参数），返回正类、负类。
def classify(inX,w):
    result=sigmoid(sum(w*inX))
    if result>0:
        return 1
    else:
        return -1
#定义划线函数
def plotBestFit(w):
    traindata,label=createData()
    dataArr = array(traindata)
    n = shape(dataArr)[0]
    w=array(w)
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
    y = (-w[0][0]-w[1][0] * x)/w[2][0]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()

#更新权值----和其他线比较---------------------------------------
def best(w,w1,traindataIn,trainlabelIn):
    trainData=mat(traindataIn)
    trainlabel=mat(trainlabelIn)
    num=0
    num1=0
    m,n=shape(trainData)
    for i in range(m):
        if(sigmoid(dot(trainData[i],w))!=trainlabel[i]):
            num=num+1
        if(sigmoid(dot(trainData[i],w1))!=trainlabel[i]):
            num1=num1+1
        i=i+1
    if num<num1:#w作为最后的结果错误比较少
        return w
    else:
        return w1
#测试集合
def classifyall(datatest,w):
    predict=[]
    for data in datatest:
        result=classify(data,w)
        predict.append(result)
    return predict
#返回权值----更新权值-------------------------------------------------
def pla(trainDataIn,trainlabelIn):
    trainData=mat(trainDataIn)
    trainlabel=mat(trainlabelIn).transpose()
    m,n=shape(trainData)
    w=ones((n,1))
    for i in range(100):
        for k in range(m):
            if (sigmoid(dot(trainData[k],w))==trainlabel[k]):
                continue
            else:
                w1=(trainlabel[k]*trainData[k]).transpose()+w
                w=best(w,w1,trainData,trainlabel)
            k=k+1
        i=i+1
    return w
#--------------------------------------
#定义main函数，测试
def main():
    trainData,label=createData()
    w=pla(trainData,label)
    plotBestFit(w)
    print (w)
if __name__=='__main__':
    start = time.clock()
    main()
    end = time.clock()
    print('finish all in %s' % str(end - start))