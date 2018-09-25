#-*- encoding:utf-8 -*-
import sys
import numpy as np
import os
import matplotlib.pyplot as plt
import random
from mlxtend.plotting import plot_decision_regions
from matplotlib import animation
reload(sys)
sys.setdefaultencoding('utf-8')
class bpnn:
    def __init__(self,a,b,c,d):
        np.random.seed(1)
        self.l0_w=np.random.random((a,b)) #输出层到隐含层的权值
        self.l1_w=np.random.random((b,c)) #隐含1层到隐含2层的权值
        self.l2_w=np.random.random((c,d)) #隐含2层到输出层的权值
    def train(self,X,Y,iterators,test_percent,lr):
        prev_loss=0
        flag=0
        for i in xrange(iterators+1):
            j=random.randint(0,len(X)-1)
            x=X[j] #取一行训练数据
            y=Y[j]
            l0=x
            l1=sigmoid(np.dot(x,self.l0_w)) #得到第一层输出
            l2=sigmoid(np.dot(l1,self.l1_w)) #得到第二层输出
            l3=sigmoid(np.dot(l2,self.l2_w))
            l3_error=l3-y
            loss=np.sqrt(np.sum(np.square(l3_error)))*100

            l2_delta=l2.T.dot(l3_error)

            self.l2_w-=lr*l2_delta
            l3_error=l3_error.transpose()
            l2_error=np.multiply(self.l2_w.dot(l3_error),sigmoid(l2,True).T) #不能省略求导,已经是输出了,所以直接相乘

            l1_error=np.multiply(self.l1_w.dot(l2_error),sigmoid(l1,True).T) #不能省略求导

            l1_delta=l1.T.dot(l2_error.T) #
            l0_delta=l0.T.dot(l1_error.T)
            self.l1_w-=lr*l1_delta
            self.l0_w-=lr*l0_delta
            if(flag%10000==0):
                if(flag!=0):
                    plt.plot([flag-10000,flag],[prev_loss,loss],'r--')
                plt.scatter(flag,loss,s=40,c='red')
                print "tranning:"+str(flag)+" times"+",total loss="+str(loss)
                prev_loss=loss
            flag=flag+1

    def predict(self,x):
        x=AutoNorm(x)
        l1=sigmoid(np.dot(x,self.l0_w))
        l2=sigmoid(np.dot(l1,self.l1_w))
        l3=sigmoid(np.dot(l2,self.l2_w))
        return l3
def AutoNorm(Z):
    Zmax,Zmin = Z.max(), Z.min()
    Z = (Z - Zmin)/(Zmax - Zmin)
    return Z
def sigmoid(x,deriv=False):
    y=1.0 / (1 + np.exp(-x))
    if(deriv==True):
        return np.multiply(x,1-x)
    return y
def load_dataset(dataset,len_x,len_y):
    dataset=open(dataset,'r')
    line=dataset.readline()
    X=list()
    Y=list()
    while line:
        l=line.strip('\n')
        l=l.split(' ')
        l = [ float( l ) for l in l if l ]
        X.append(l[0:len_x])
        Y.append(l[len_x:len_x+len_y])
        line=dataset.readline()
    return (X,Y)
if __name__=="__main__":
    degree1=4
    degree2=4
    newnn=bpnn(4,degree1,degree2,2)
    (X,Y)=load_dataset('IrisData.txt',4,2)
    X=np.matrix(X)
    Y=np.matrix(Y)
    X=AutoNorm(X)
    y=list()
    for i in Y:
        y.append(i.tolist()[0][0])
    plt.figure(2)
    plt.xlabel("epoch times")
    plt.ylabel("loss rate")
    plt.title("total loss rate graph")
    #ax1=plt.subplot(211)
    #ax2=plt.subplot(212)
    newnn.train(X,Y,60000,0.3,0.035)
    #plt.sca(ax1)
    #plot_decision_regions(X,y,newnn,legend=1)
    #plt.title("Decision Boundary for hidden layer size %d"%degree)
    plt.savefig('E:\\ml\\iris.jpg')
    print newnn.predict(np.matrix([6.7,3.1,4.4,1.4]))
    plt.show()