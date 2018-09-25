# -*- coding: utf-8 -*-




"""
In the general case, we have a "target function" that we want to minimize,
and we also have its "gradient function". Also, we have chosen a starting
value for the parameters "theta_0".
"""
from numpy import *

###读取data  第二章  k近邻
##将文本记录转换为Numpy
def file2matrix(filename):
    ##得到文件行数
    fr = open(filename)  # 打开文件，按行读入
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)  # 获得文件行数
    ##创建返回的Numpy矩阵
    returnMat = zeros((numberOfLines, 3))  # 创建m行3列的零矩阵
    classLAbelVector = []
    index = 0
    ##解析文件数据到列表(循环处理文件中每行数据)
    for line in arrayOLines:
        line = line.strip()  # 删除行前面的空格(截取掉所有的回车字符)
        listFormLine = line.split('\t')  # 根据分隔符划分(使用tab字符\t将上步得到的整行数据分割成一个元素列表)

        returnMat[index, :] = listFromLine[0:3]  # 取得每一行的内容存起来(选取前三个元素，将它们存储到特征矩阵中)
        classLabelVector.append(
            int(listFromLine[-1]))  # Python语言可以使用索引值-1表示列表中最后一个元素，很方便的将列表最后一列存储到向量classLabelVector中）
        index += 1  # (需要注意的是，必须明确通知解释器，告诉它，列表中存储的元素值为整型，否则，Python将它们视为字符串处理)

    return returnMat, classLabelVector  # 归一化数据


#将图像转换为测试向量
def img2vector(filename):
    returnVect = zeros((1,1024))         #创建 1*1024的numpy数组
    fr = open(filename)
    for i in range(32):                   #读取文件前32行
        linestr = fr.readline()           #readline每次只读取一行
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])      #将每行头32个字符值存在numpy数组中
    return returnVect



#### 第八章 回归
###将txt文本转换文训练矩阵,加载数据集。
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')    #得到每行，并以tab作为间隔

        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat



####第十章 k-均值聚类算法
####数据导入函数
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine)     #map all elements to float()
        dataMat.append(fltLine)
    return dataMat

