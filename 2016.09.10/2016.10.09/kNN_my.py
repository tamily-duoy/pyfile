# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 19:05:33 2016

@author: Administrator
"""

from numpy import *   #科学计算包
import operator
from os import listdir       #从OS模块中导入listdir，它可以列出给定目录的文件名(这个函数可以返回一个文件夹里面所有文件的文件名)

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
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1  #get(key,default=None),就是造字典
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
    classLAbelVector = []
    index = 0
    ##解析文件数据到列表(循环处理文件中每行数据)
    for line in arrayOLines:
        line = line.strip()        #删除行前面的空格(截取掉所有的回车字符)
        listFormLine = line.split('\t')    #根据分隔符划分(使用tab字符\t将上步得到的整行数据分割成一个元素列表)
        
        returnMat [index,:] = listFromLine[0:3]   #取得每一行的内容存起来(选取前三个元素，将它们存储到特征矩阵中)
        classLabelVector.append(int(listFromLine[-1])) #Python语言可以使用索引值-1表示列表中最后一个元素，很方便的将列表最后一列存储到向量classLabelVector中）
        index += 1                                         #(需要注意的是，必须明确通知解释器，告诉它，列表中存储的元素值为整型，否则，Python将它们视为字符串处理)
        

    return returnMat,classLabelVector      #归一化数据
    

    
    
    
# datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
# testVector = kNN.img2vector('testDigits/0_13.txt')
# #使用matplotlib创建散点图(python命令行环境)
# import matplotlib
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2],
#               15.0*array(datingLabels), 15.0*array(datingLabels))
#         #利用变量datingLabels存储的类标签属性，在散点图上绘制色彩不等，尺寸不同的点
# plt.show()
#
#

#
# #将任意取值范围内的特征值转化为 0 到 1 区间内的值
# newValue = (oldValue-min)/(max-min)
# #在文件kNN.py中增加新函数 autoNorm() ，该函数可自动将数字特征转化为 0 到 1 的区间

###归一化特征值
def autoNorm(dataSet):
    minVals = dataSet.min(0)      #每列的最小值放在变量minVals中，dataSet.min(0)，0使函数从列中选出最小值，而不是行
    maxVals = dataSet.max(0)      #每列的最大值放在变量maxVals中
    ranges = maxVals - minVals    #函数计算可能的取值范围
    normDataSet = zeros(shape(dataSet))   #创建新的返回矩阵
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1)) #因特征值矩阵有1000*3个值，而minVals和range的值都为1*3，所以用tile将变量内容复制成输入矩阵同样大小的矩阵
    normDataSet = normDataSet/title(ranges,(m,1)) #这是具体特征值相除(/有时表示矩阵除法)
                 #Numpy中，矩阵除法：linalg.solve(matA,matB)
    return normDataSet,  ranges,minvals

#
# ####检测函数执行结果(python命令行环境)
# reload(kNN)
# normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
# normMat  #---
# ranges #---
# minVals  #---
#

###测试分类器效果，在kNN.py中创建函数datingClassTest，该函数是自包含的，可任何时候在Python运行环境中使用该函数测试分类器效果
def datingClassTest():
    hoRatio = 0.10                  # 设定用于测试的数据比例
    datingDataMat,DatingLabels = file2matrix('datingTestSet.txt')    # 导入数据
    normMat, ranges, minVals = autoNorm(datingDataMat)               # 归一化
    m = normMat.shape[0]             # 一共的数据条目数
    numTestvecs = int(m*hoRatio)    #计算测试向量的数量，决定normMat中哪些数据用于测试，哪些用于训练(  # 用于测试的条目)
    errorCount = 0.0                # 初始化错误率
    for i in range(numTestVecs):    # 循环读取每行数据
        classifierResult = classfy0(normMat [i,:],normMat [numTestVecs:m,:],datingLabels[numTestVecs:m],3)    #\       # 对该测试条目进行分类
                                    # datingLabels[numTestVecs:m],3)
        print "the classifer came back with : %d, the real answer is: %d" % (classifierResult,datingLabels[i])    #\              # 打印分类结果与真实结果
                   # % (classifierResult,datingLabels[i])
    if (classifierResult != datingLabels[i]): errorCount +=1.0                           # 比较分类结果与真实结果
    print "the total error rate is : %f " % (errorCount/float(numTestVecs))


def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']           #结果列表：不喜欢、魅力一般、极具魅力
    ffMiles = float(raw_input("frequent flier miles earned per year:"))               #输入每年获得的飞行常客里程数
    percentTats = float(raw_input("percentage of time spent playing video games:"))   #输入视频游戏所耗时间百分比
    iceCream = float(raw_input("liters of ice cream consumed per week:"))             #输入每周消费的冰淇淋公升数
    datingDataMat,datingLabels = file2matrix('datingTestSet.txt')           #调用文本转换矩阵函数
    normMat,ranges,minVals = autoNorm(datingDataMat)                        #对数据进行归一化
    inArr = array([ffMiles,percentTats,iceCream])                           #将输入数据写入数组中
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)      #调用分类器
    print "You will probably like this person: ",resultList[classifierResult -1]   #这边减1是由于最后分类的数据是1，2，3对应到数组中是0，1，2



def img2vector(filename):
    returnVect = zeros((1,1024))         #创建 1*1024的numpy数组
    fr = open(filename)
    for i in range(32):                   #读取文件前32行
        linestr = fr.readline()           #readline每次只读取一行
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])      #将每行头32个字符值存在numpy数组中
    return returnVect


def handwritingClassTest():
#### 训练数据
    hwLabels = []    #列表
    trainingFileList = listdir('trainingDigits')       #获取文件内容，将目录文件内容存储到列表(返回文件夹里，所有文件的文件名)
    m = len(trainingFileList)                          #目录中有多少文件
    trainingMat = zeros((m,1024))                      #创建m行，1024列训练矩阵，每行数据存储一个图像
    for i in range(m):
        fileNameStr = trainingFileList[i]               #读取文件名，切割得到标签  从文件名称解析得到分类数据
        fileStr = fileNameStr.split('.')[0]             # 0_13.txt是 0 的第十三个特例
        classNumStr = int(fileStr.split('_')[0])        # 0_13.txt 的分类是 0
        hwLabel.append(classNumStr)                     #将类代码存储在向量 hwLabels中
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)   #载入图像
##### 测试数据
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat,hwLabels,3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult,classNumStr)
        if(classifierResult != classNumStr): errorCount +=1.0
    print "\nthe total number of error is:%d" % errorCount
    print "\nthe total error rate is:%f" % (errorCount/float(mTest))


