# -*- coding: utf-8 -*-




"""
In the general case, we have a "target function" that we want to minimize,
and we also have its "gradient function". Also, we have chosen a starting
value for the parameters "theta_0".
"""

from numpy import *

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

####计算回归系数
###计算最佳拟合曲线。
def standRegres(xArr,yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:  # numpy提供一个线性代数的库linalg 。直接调用linalg.det（)来计算行列式。
        print "This matrix is singular, cannot do inverse "
        return
####求回归系数。
    ws = xTx.I * (xMat.T*yMat)  #numpy还提供解未知矩阵的函数 ws = linalg.solve (xTx,xMat.T*yMatT) 。   .I 是求逆矩阵。
    return ws     #ws相关系数，此处ws存放的是回归系数。

# ### import regression_my
# from numpy import *
# xArr, yArr = regression_my.loadDataSet('ex0.txt')
# xArr[0:2]
# ws = regression_my.standRegres(xArr,yArr)
# ws
# xMat = mat(xArr)
# yMat = mat(yArr)
# yHat = xMat *ws   最终得到y = ws[0]x0+ws[1]*x1  ,用内积来预测y的时候，第一维将乘以前面的常数x0,第二维将乘以输入变量x1 。
                    # 这里的y实际上是预测出来的，为了和真实值区分开来，用yHat表示 。  x0 是为了计算方便给出的。



###numpy 库提供了相关系数的计算方法：可通过命令corrcoef(yEstimate,yActual)来计算预测值和真实值之间的相关性。
# yHat = xMat * ws    #求相关系数的命令。
# corrcoef(yHat.T, yMat)
#返回： array([[ 1.        ,  0.98647356],
#        [ 0.98647356,  1.        ]])         #yMat是预测值。
#可看到，对角上数据是1 ，因为yMat和自己配是最完美的，而yHat和yMat的相关系数为0.98 。



#线性回归，可能出现欠拟合，因为它求的是最小均方误差（因为求得的是，使误差最小的 w 的值）的无偏估计。
#因此，有些方法允许在估计中引入一些偏差（直线估计变为曲线估计），从而降低预测的均方误差。
#####局部加权线性回归函数

def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat = mat(xArr) ; yMat = mat(yArr).T    #原始数据集转化为矩阵。
    m = shape(xMat)[0]       #xArr的行数。
    weights = mat(eye((m)))  #产生对角矩阵，初始化权重矩阵为m行m列的全1单位矩阵。
    for j in range(m):     #接下来两行创建权重矩阵
        diffMat = testPoint - xMat[j, :]   #（下一行）利用高斯核函数计算权重矩阵，计算后的权重是一个对角阵。
        weights [j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))  #更新权重值，以指数级递减。
        xTx = xMat.T * (weights * xMat)
        if linalg.det(xTx) ==0:
            print "This matrix is signgular,cannot do inverse"  #矩阵为奇异矩阵，没有逆。
            return
        ws = xTx.I *(xMat.T * (weights * yMat))
        return testPoint * ws           #计算回归线坐标矩阵。
#为数据集中的每个点调用lwlr()，有助于求解k的大小
def lwlrTest(testArr,xArr,yArr,k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat [i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat



# reload(regression_my)
# xArr, yArr = regression_my.loadDataSet('ex0.txt')
# yArr[0]
# regression_my.lwlr(xArr[0],xArr,yArr,1.0)
# regression_my.lwlr(xArr[0], xArr, yArr, 0.001)
# yHat = regression_my.lwlrTest(xArr, xArr, yArr, 0.003)
# xMat = mat(xArr)
# srtInd = xMat[:,1].argsort(0)      #按序排列绘图所需数据点。[取出整个数组（行），索引为1的元素] . 按列排序。
# xSort = xMat[srtInd][:,0,:]       #[上步得到的列表][取出整个数组（行），索引为1，全部元素]
#最后两步得到，[x0 ,x1] 两列按升序排列的数组列。

# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)           #111表示将画布划分为1行2列选择使用从上到下第一块
# ax.plot(xSort[:,1],yHat[srtInd])
# ax.scatter(xMat[:,1].flatten().A[0],mat(yArr).T.flatten().A[0],s=2,c='red')
# plt.show()



####预测鲍鱼的年龄
#使用平方误差，分析预测误差大小
def rssError(yArr,yHatArr):
    return((yArr-yHatArr)**2).sum()

# abX,abY = regression_my.loadDataSet('abalone.txt')   #最后一列为YArr,前面其余为xArr。
# yHat1 =  regression_my.lwlrTest(abX[0:99],abX[0:99],abY[0:99],1)
# yHat10 =  regression_my.lwlrTest(abX[0:99],abX[0:99],abY[0:99],10)
# yHat01 =  regression_my.lwlrTest(abX[0:99],abX[0:99],abY[0:99],0.1)

# regression_my.rssError(abY[0:99],yHat01.T)
# regression_my.rssError(abY[0:99],yHat1.T)
# regression_my.rssError(abY[0:99],yHat10.T)

# yHat = regression_my.lwlrTest(abX[100:199],abX[0:99],abY[0:99],0.1)
# regression_my.rssError(abY[100:199],yHat01.T)
# yHat = regression_my.lwlrTest(abX[100:199],abX[0:99],abY[0:99],1)
# regression_my.rssError(abY[100:199],yHat1.T)
# yHat = regression_my.lwlrTest(abX[100:199],abX[0:99],abY[0:99],10)
# regression_my.rssError(abY[100:199], yHat10.T)
#
# ws = regression_my.standRegres(abX[0:99],abY[0:99])
# yHat = mat(abX[100:199]) * ws
# regression_my.rssError(abY[100:199],yHat.T.A)



###岭回归，给定lam下的岭回归。
##计算ws的值。实现给定lam下岭回归求解。
#如果没有指定lam，则默认为0.2
def ridgeRegres(xMat,yMat,lam = 0.2):
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * lam  # x的转置*x + lam * 单位矩阵I
    if linalg.det(denom) ==0.0:    #检查行列式值是否为 0 的原因:lam可能为 0 。
        print "This matrix is singular, cannot do inverse"
        return
    ws = denom.I * (xMat.T*yMat)
    return ws
#用于在一组lam上测试结果。
#数据的标准化过程，具体过程就是所有特征都减去各自的均值并处理方差。
def ridgeTest(xArr,yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    yMean = mean(yMat,0)       #按照行取平均，每行平均。
    yMat = yMat - yMean        #对y进行标准化(各行每一元素 - 各行的均值)。
    xMeans = mean(xMat,0)
    #计算xMat的样本方差。
    xVar = var(xMat,0)           #按行取方差
    xMat = (xMat - xMeans)/xVar  #对数据进行标准化。
    numTestPts = 30
    wMat = zeros((numTestPts,shape(xMat)[1]))
    for i in range(numTestPts):    #进行numTestPts次计算岭回归，每次的系数向量都放到wMat的一行中。
        ws = ridgeRegres(xMat,yMat,exp(i-10))   #参数lam每次以exp(i-10)变化
        wMat[i,:] = ws.T
    return wMat
# #ridgeWeights,为30*8的矩阵，
# 对矩阵画图，则以每列为一个根线，为纵坐标，
# 横坐标为range(shape(ridgeWeights)[0])也即从0到29,
# 第一行的横坐标为0,最后一行的行坐标为29

#reload(regression_my)
# abX, abY = regression_my.loadDataSet('abalone.txt')
#ridgeWeights = regression_my.ridgeTest(abX,abY)

# import matplotlib.pyplot as plt
#fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(ridgeWeights)
# plt.show()


##定义正则化，按照均值为0，方差为 1 ，对列进行标准化处理。
def regularize(xMat):
    inMat = xMat.copy()
    inMeans = mean(inMat, 0)
    #求方差
    inVar = var(inMat,0)
    inMat = (inMat - inMeans) / inVar
    return inMat

####向前逐步线性回归
#eps：每次迭代需要调整的步长
#numIt：迭代的次数
def stageWise(xArr,yArr,eps = 0.01,numIt=100):
    xMat = mat(xArr);yMat = mat(yArr).T
    yMean = mean(yMat,0)
    yMat = yMat - yMean
    #按照均值为0，方差为1，进行标准化处理
    xMat = regularize(xMat)
    m, n = shape(xMat)
    returnMat = zeros((numIt,n))
    ws = zeros((n,1))
    wsTest = ws.copy(); wsMax = ws.copy()  #为实现贪心算法，建立了ws的两个副本
    #贪心算法在所有特征上运行两次for循环，
    # 分别计算增加或减少该特征对误差的影响，这里使用平方误差。
    for i in range(numIt):
        print ws.T
        #误差初始值设为正无穷
        lowestError = inf;
        for j in range(n):
            for sign in [-1,1]:
                wsTest = ws.copy()
                wsTest[j] +=eps * sign
                yTest = xMat * wsTest
                rssE = rssError(yMat.A,yTest.A)
                if rssE < lowestError:
                    lowestError = rssEwsMax = wsTest
        ws = wsMax.copy()
        returnMat[i,:] = ws.T
    return returnMat
