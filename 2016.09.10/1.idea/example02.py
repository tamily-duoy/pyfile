# -*- coding: utf-8 -*-
from numpy import *
import operator


def creatDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels


def classify0(inX,dataSet,labels,k): # inX用于需要分类的数据，dataSet输入训练集


    ######输入与训练样本之间的距离计算######
    dataSetSize = dataSet.shape[0] # 读取行数,shape[1]则为列数
    diffMat = tile(inX,(dataSetSize,1))-dataSet # tile,重复inX数组的行(dataSize)次，列重复1
    sqDiffMat = diffMat**2 #平方操作
    sqDistances = sqDiffMat.sum(axis=1) # 每一个列向量相加,axis=0为行相加
    distances = sqDistances**0.5

    sortedDistIndicies = distances.argsort() # argsort函数返回的是数组值从小到大的索引值
    #print sortedDistIndicies #产生的是一个排序号组成的矩阵
    classCount={}

    ######累计次数构成字典######
    for i in range(k):
        #print sortedDistIndicies[i]
        voteIlabel = labels[sortedDistIndicies[i]] #排名前k个贴标签
        #print voteIlabel
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1 # 不断累加计数的过程，体现在字典的更新中
        #print classCount.get(voteIlabel,0)
        #print classCount
        #get(key,default=None),就是造字典


    ######找到出现次数最大的点######
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse=True)
    #以value值大小进行排序，reverse=True降序
    #print classCount.iteritems()
    #print sortedClassCount
    #key = operator.itemgetter(1)，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值

    return sortedClassCount[0][0]




# -*- coding: utf-8 -*-
import example02

group,labels = example02.creatDataSet() # 调用Knn_bymyself中的creatDataSet()方法
while 1:
    try:
        a=input('please input x:')
        b=input('please input y:')
        #classify0(inX,dataSet,labels,k)对应起来看
        print 'belong to :' % example02.classify0([a,b],group,labels,3)+' class'
    except:
        break