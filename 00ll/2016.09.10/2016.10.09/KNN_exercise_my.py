# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:05:33 2016

@author: Administrator
"""

from numpy import *   #科学计算包
import operator       #运算符模块

def creatDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])  #创建数据集
    labels=['A','A','B','B']                          #创建标签
    return group,labels
    
                                          #inX,用于分类的输入向量。即将对其进行分类。
def classify0(inX,dataSet,labels,k):  # inX用于需要分类的数据，dataSet输入训练集
######输入与训练样本之间的距离计算######
    dataSetSize=dataSet.shape[0]    # 读取数据集行数,shape[1]则为列数
    diffMat=tile(inX,(dataSetSize,1)) -dataSet
                 #tile:numpy中的函数。tile将原来的一个数组，扩充成了4个一样的数组。
                 #diffMat得到了目标与训练数值之间的差值。
    sqDiffMat=diffMat**2            #各个元素分别平方  
    sqDistances=sqDiffMat.sum(axis=1)  # 每一个列向量相加,axis=0为行相加  
                                       #对应列相乘，即得到了每一个距离的平方
    distances=sqDistances**0.5         #开方，得到距离。
    sortedDistIndicies=distances.argsort()   #升序排列
 #选择距离最小的k个点。
    classCount={}
    for i in range (k):
        voteIlabel=labels[sortedDistIndicies[i]]  #排名前k个贴标签
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1#get(key,default=None),就是造字典
 ######找到出现次数最大的点######
  #以value值大小进行排序，reverse=True降序
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
 #key = operator.itemgetter(1)，operator.itemgetter函数
 #获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值
    return sortedClassCount [0] [0]
  #返回出现次数最多的value的key
  
  
  
  
 ###读取data 
def file2matrix(filename):
    ##得到文件行数
    fr=open(filename)                  #打开文件，按行读入
    arrayOLines=fr.readlines()      
    numberOfLines=len(arrayOLines)      #获得文件行数 
    ##创建返回的Numpy矩阵
    returnMat=zeros((numberOfLines,3))   #创建m行3列的零矩阵
    classLabelVector = []
    index = 0
    ##解析文件数据到列表(循环处理文件中每行数据)
    for line in arrayOLines:
        line = line.strip()        #删除行前面的空格(截取掉所有的回车字符)
        listFormLine = line.split('\t')    #根据分隔符划分(使用tab字符\t将上步得到的整行数据分割成一个元素列表)
        
        returnMat [index,:] = listFormLine[0:3]   #取得每一行的内容存起来(选取前三个元素，将它们存储到特征矩阵中)
        classLabelVector.append(int(listFormLine[-1])) #Python语言可以使用索引值-1表示列表中最后一个元素，很方便的将列表最后一列存储到向量classLabelVector中）
        index += 1
        

    return returnMat,classLabelVector      #归一化数据
    

# datingDataMat,DatingLabels = kNN.file2matrix('datingTestSet.txt')
datingDataMat,DatingLabels = file2matrix('datingTestSet.txt')
    
    
    
# #使用matplotlib创建散点图(python命令行环境)
# import matplotlib
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:1],datingDataMat[:,2])
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2],
#               15.0*array(datingLabels), 15.0*array(datingLabels))
#         #利用变量datingLabels存储的类标签属性，在散点图上绘制色彩不等，尺寸不同的点
# plt.show()




# #将任意取值范围内的特征值转化为 0 到 1 区间内的值
# newValue = (oldValue-min)/(max-min)
# #在文件kNN.py中增加新函数 autoNorm() ，该函数可自动将数字特征转化为 0 到 1 的区间

###归一化特征值
def autoNorm(dataSet):
    minVals = dataSet.min(0)      #每列的最小值放在变量minVals中，dataSet.min(0)，0使函数从列中选出最小值，而不是行
    maxVals = dataSet.max(0)      #每列的最大值放在变量maxVals中( # 每列中最大值和最小值取出)
    ranges = maxVals - minVals    #函数计算可能的取值范围( # 最大值与最小值范围作为归一化的分母)
    normDataSet = zeros(shape(dataSet))   #创建新的返回矩阵(  # 初始化归一化后的矩阵)
    m = dataSet.shape[0]                  # 数据条目数目
    normDataSet = dataSet - tile(minVals,(m,1)) #因特征值矩阵有1000*3个值，而minVals和range的值都为1*3，所以用tile将变量内容复制成输入矩阵同样大小的矩阵
    normDataSet = normDataSet/title(ranges,(m,1)) #这是具体特征值相除(/有时表示矩阵除法)         (    # 归一化)
                 #Numpy中，矩阵除法：linalg.solve(matA,matB)
    return normDataSet,  ranges,minvals

#
# ####检测函数执行结果(python命令行环境)
# reload(kNN)
# normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
# normMat  #---
# ranges #---
# minVals  #---


###测试分类器效果，在kNN.py中创建函数datingClassTest，该函数是自包含的，可任何时候在Python运行环境中使用该函数测试分类器效果
def datingClassTest():
    hoRatio = 0.10     #设定用于测试的数据比例
    filename = 'datingTestSet2.txt'             # 导入数据
    datingDataMat,DatingLabels = file2matrix('datingTestSet.txt')   #从文件中加载数据集
    normMat, ranges, minVals = autoNorm(datingDataMat)               # 归一化
    m = normMat.shape[0]                                             # 一共的数据条目数
    numTestvecs = int(m*hoRatio)     #计算测试向量的数量，决定normMat中哪些数据用于测试，哪些用于训练(# 用于测试的条目)
    errorCount = 0.0                 # 初始化错误率
    for i in range(numTestVecs):     # 循环读取每行数据
        classifierResult = classfy0(normMat [i,:],normMat [numTestVecs:m,:], datingLabels[numTestVecs:m],3)    #对该测试条目进行分类
                                    #datingLabels[numTestVecs:m],3)       #here set k=3
        print "the classifer came back with : %d, the real answer is: %d" % (classifierResult,datingLabels[i])     # 打印分类结果与真实结果
                #   % (classifierResult,datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount +=1.0                  # 比较分类结果与真实结果
    print "the total error rate is : %f" % (errorCount/float(numTestVecs))

def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']               #结果列表：不喜欢、魅力一般、极具魅力
    percentTats = float(raw_input("percentage of time spent playing video games?"))  # #输入每年获得的飞行常客里程数
    ffMiles = float(raw_input("frequent flier miles earned per year?"))              #输入视频游戏所耗时间百分比
    iceCream = float(raw_input("liters of ice cream consumed per year?"))            #输入每周消费的冰淇淋公升数
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')             #调用文本转换矩阵函数
    normMat, ranges, minVals = autoNorm(datingDataMat)                          #对数据进行归一化
    inArr = array([ffMile,percentTats,iceCream])                               #将输入数据写入数组中
    classiferResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)  #调用分类器
    print "you will probably like this person:",resultList[classiferResult - 1]   #这边减1是由于最后分类的数据是1，2，3对应到数组中是0，1，2




