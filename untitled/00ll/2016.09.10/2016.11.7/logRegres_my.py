# -*- coding: utf-8 -*-
"""
In the general case, we have a "target function" that we want to minimize,
and we also have its "gradient function". Also, we have chosen a starting
value for the parameters "theta_0".
"""

####logistic回归梯度上升优化算法
##加载数据，返回矩阵
from numpy import *

def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()          #下一行：对原始数据做了拓展，将两维拓展为三维，第一维全部设置为1.0
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])   #为了方便，Xo设为1，接着X1,x2
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

##定义sigmoid函数：
def sigmoid(inX):
    return 1.0/(1+exp(-inX))

##定义梯度上升函数
##用整个数据集更新参数。
def gradAscent(dataMatIn,classLabels):        #两个参数。第一个：二维numpy数组，每列--不同特征值；每行--每个样本。（此处加了第0行特征值，x0=1）。
    # dataMatIn是一个三列矩阵。                           第二个：1x100的行向量，为便于计算，转化为列向量。
    dataMatrix =mat(dataMatIn)                #转换为numpy矩阵，数值类型。
    labelMat = mat(classLabels).transpose()    #行向量转化为列向量,转置。
    m, n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))            #权重初始化为1，个数 = 特征值个数。
    # ##由于在定义weights时是采用weights=ones(n,3)#进而需要在后续调用时加上getA()函数，以免出错
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)  #此处往下，是 矩阵运算。    h是一个列向量。
        error = (labelMat - h)
        weights = weights + alpha*dataMatrix.transpose()*error
    return weights
###运行代码
import logRegres_my
dataArr, labelMat = logRegres_my.loadDataSet()
#logRegres_my.gradAscent(dataArr,labelMat)


####画出数据集和logistic回归最佳拟合直线的函数
##定义最佳拟合直线函数
def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])  #挑出标签为 1 的数据。放到上述创建的列表。
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])  #挑出标签为 0 的数据。
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30,c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')   #下一行，-3到3，以步长为0.1迭代。
    x = arange(-3.0, 3.0, 0.1)             #下一行：解出 x1 和 x2 的关系式。x2即此处的 Y 。
    y = (-weights[0]-weights[1]*x/weights[2])     #  weights[0]*1.0+weights[1]*x+weights[2]*y=0  \z=0,此时sigmoid = 0.5
    ax.plot(x, y)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.show()
###运行代码
from numpy import *
reload(logRegres_my)
weights = logRegres_my.gradAscent(dataArr, labelMat)
#logRegres_my.plotBestFit(weights.getA())
#上述程序中有很多人不太明白weights.getA()这句是什么意思，调试时，如果直接print weights和print weights.getA()
#会发现输出结果是一样的，但是如果将程序改为logRegres.plotBestfit(weights)会发现程序出错
#原因就在于，python的科学计算库numpy中定义了一种ndarray，这种数组是一种描述性数组。
# 对这种描述性数组用getA()得到的结果是其本身，但是在程序执行过程中调用机制是不一样的

####随机梯度上升算法
##区别：一次仅用一个样本点更新参数。
def stocGradAscent0(dataMatrix, classLabels):
    m, n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)
    for i in range(m):           # m = 100        # 区别：没有矩阵转换过程，所有变量的数据类型都是numpy数组。
        h = sigmoid(sum(dataMatrix[i]*weights))   # 区别：是数值而不再是向量。单个样本的 h 值。
        #print dataMatrix[i]
        error= classLabels[i] - h                 # 区别：是数值而不再是向量
        weights = weights + alpha* error * dataMatrix[i]
    return weights

from numpy import *
reload(logRegres_my)
dataArr, labelMat = logRegres_my.loadDataSet()
weights = logRegres_my.stocGradAscent0(array(dataArr),labelMat)
#logRegres_my.plotBestFit(weights)

####改进的随机梯度上升算法
##改进一：alpha在每次迭代时都会调整===缓解数据波动或高频波动；（增加常数项，使得：alpha不会随迭代次数变为0===常数项的控制=控制新样本对回归系数的影响。）
##改进二：随机选取样本来更新回归系数====减少周期性波动；
##改进三：增加迭代系数为参数===迭代次数可控。
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m, n = shape(dataMatrix)
    weights = ones(n)
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i) + 0.01
            randIndex = int(random.uniform(0,len(dataIndex)))      #random.uniform(x, y)随机数的最小值、最大值。
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights +alpha * error * dataMatrix[randIndex]
    return weights


reload(logRegres_my)
dataArr,labelMat = logRegres_my.loadDataSet()
weights = logRegres_my.stocGradAscent1(array(dataArr),labelMat,150)
#logRegres_my.plotBestFit(weights)

####用logistics回归进行分类（病马：从病症预测马的死亡率）
##定义分类向量
def classifyVector(inX, weights):  #回归系数和特征向量作为输入，来计算对应的sigmoid值。
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5:                 #sigmoid值大于0.5，则返回 1 ，否则返回 0 。
        return 1.0
    else:
        return 0.0

##原始数据预处理后，保存成两个文件：horseColicTest.txt和horseColicTraining.txt 。   22列数据。
##定义ColicTest，用于打开训练集和测试集。并 对数据格式化处理。
def colicTest():
    frTrain = open('horseColicTraining.txt')  #读取训练集
    frTest = open('horseColicTest.txt')       #读取测试集
    trainingSet = []                 #创建训练集
    trainingLabels = []              #创建训练标签
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscent1(array(trainingSet), trainingLabels, 1000)   # 调用stocGradAscent1，来计算回归系数向量。
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights))!= int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount)/numTestVec)
    print "the error rate of this test is: %f" % errorRate
    return errorRate

##定义multiTest 。功能：调用ColicTest函数10次，并求结果的平均值。
def multiTest():
    numTests = 10;
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print "after %d iterations the average error rate is: %f" % (numTests, errorSum / float(numTests))  # 返回结果的均值。

reload(logRegres_my)
#logRegres_my.multiTest()

