# -*- coding: utf-8 -*-




"""
In the general case, we have a "target function" that we want to minimize,
and we also have its "gradient function". Also, we have chosen a starting
value for the parameters "theta_0".
"""

####单层决策树生成函数
from numpy import *
# 加载数据集
def loadSimpData():
    #样本特征
    datMat = matrix([[1.0,2.1],
                     [2.0,1.1],
                     [1.0,1.0],
                     [2.0,1.0]])
    #正负样本标志
    classLabels = [1.0,1.0,-1.0,-1.0,1.0]
    return datMat, classLabels

# ### main 函数,可以打印出结果
# if __name__=="__main__":
#     datMat,classLabels = loadSimpData()
#     print "datMat:",datMat
#     print "classLabels:",classLabels
###键入以下命令，可以实现数据集和类标签的导入
# import adaboost
# datMat,classLabels = adaboost.loadSimpData()

####单层决策树生成函数
def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArray = ones((shape(dataMatrix)[0],1))
    if threshIneq =='It':
        retArray[dataMatrix[:,dimen] <=threshVal] = -1.0
    else:
        retArray[dataMatrix[:,dimen] > threshVal] = -1.0
    return retArray

def buildStump(dataArr,classLabels,D):
    dataMatrix = mat(dataArr); labelMat = mat(classLabels).T
    m,n = shape(dataMatrix)
    numSteps = 10.0 ;bestStump= mat(zeros((m,1)))
    minError = inf
    for i in range(n):
        rangeMin = dataMatrix[:,i].min();rangeMax = dataMatrix[:,i].max();
        stepSize = (rangeMax - rangeMin)/numSteps
        for j in range(-1,int(numSteps)+1):
            for inequal in ['It','gt']:
                threshVal = (rangeMin + float(j)*stepSize )
                predictedVals = \
                    stumpClassify(dataMatrix,i,threshVal,inequal)
                errArr = mat(ones((m,1)))
                errArr[predictedVals == labelMat] = 0
                weightedError = D.T*errArr
                print "split: dim %d, thresh %.2f, thresh ineqal:%s, the weighted error is %.3f" % (i,threshVal,inequal,weightedError)
            if weightedError <minError:
                minError = weightedError
                bestClassEst = predictedVals.copy()
                bestStump['dim'] = i
                bestStump['thresh'] = threshVal
                bestStump['ineq'] = inequal
    return bestStump,minError,bestClassEst


####
####

###ROC曲线的绘制及AUC计算函数
def plotROC(predStrengths,classLabels):
    import matplotlib.pyplot as plt
    cur = (1.0,1.0)         # cur保留的是绘制光标的位置,初始化。
    ySum = 0.0              # ySum则用于计算AUC的值，即ROC曲线的面积，初始化。
    numPosClas = sum(array(classLabels)==1.0)     # 通过数组过滤方式计算正例的数目，并赋给numPosClas。在x轴和y轴的0.0到1.0区间上绘点，确定在Y坐标轴上部进数目。
    yStep = 1/float(numPosClas)                   # 在y轴上的步长： 1/正例数目。
    xStep = 1/float(len(classLabels)-numPosClas)  # 在x轴上的步长: 1/（全-正例数目）。
    sortedIndicies = predStrengths.argSort()       # 获取排好序的索引sortedIndicies，这些索引从小到大排序。需要从<1, 1>开始绘，一直到<0,0>
   #构建画笔#
    fig = plt.figure()
    fig.clf()           #清除当前图像窗口。
    ax = plt.subplot(111)
    # 在所有排序值上进行循环。这些值在一个NumPy数组或矩阵中进行排序。
    # python则需要一个表来进行迭代循环，因此需要调用tolist()方法。
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] == 1.0:    # 每得到一个标签为1.0的类，则要沿着y轴的方向下降一个步长，即降低真阳率
            delX = 0; delY = yStep;
        else:                             # （代码只关注1这个类别标签，采用1/0标签还是+1/-1标签就无所谓了。）
            delX = xStep; delY = 0;      # 对于每个其他的标签，则是x轴方向上倒退一个步长（假阴率方向）。
            ySum += cur[1]               # 一旦决定了在x轴还是y轴方向上进行移动，就可在当前点和新点之间画出一条线段，更新当前点cur。
        ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY],c='b')   # 0 表示横坐标，1 表示纵坐标。
        cur = (cur[0]-delX,cur[1]-delY)
        ax.plot([0,1],[0,1],'b--')
        plt.xlabel('False Positive Rate'); plt.ylabel('True Positive Rate')
        plt.title('ROC curve for AdaBoost HorseColic Detection System')
        ax.axis([0,1,0,1])
        plt.show()
        # 计算AUC需要对多个小矩形的面积进行累加，这些小矩形的宽度都是xStep。
        # 因此可对所有矩形的高度进行累加，然后再乘以xStep得到其总面积。
        print "the Area Under the Curve is: ",ySum* xStep
        print "the Area Under the Curve is: ",ySum* xStep