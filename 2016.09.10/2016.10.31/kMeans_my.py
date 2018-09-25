# -*- coding: utf-8 -*-
"""
In the general case, we have a "target function" that we want to minimize,
and we also have its "gradient function". Also, we have chosen a starting
value for the parameters "theta_0".
"""
#### K-均值聚类支持函数
from numpy import *
#import kMeans_my
#from numpy import *



#import kMeans_my
#from numpy import *

###导入数据
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine)     #map all elements to float()
        dataMat.append(fltLine)
    return dataMat
#dataMat = mat(kMeans_my.loadDataSet('testSet.txt'))
#定义两个向量的欧氏距离。
def distEclud(vecA,vecB):

    return sqrt(sum(power(vecA-vecB,2)))

## 构建簇质心   #初始化k个簇的质心函数centroid
#传入的数据是Numpy的矩阵格式。
def randCent(dataSet,k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])  #找出矩阵dataMat第J列最小值。
        rangeJ = float(max(dataSet[:,j])-minJ) #计算第J列最大值最小值之差。
        #赋予一个随机质心，它的值在整个数据集的边界之内。
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)
    return centroids   #返回一个随机的质心矩阵


import kMeans_my
from numpy import *
dataMat = mat(kMeans_my.loadDataSet('testSet.txt'))
# min(dataMat[:,0])
# min(dataMat[:,1])
# max(dataMat[:,1])
# max(dataMat[:,0])
#kMeans_my.randCent(dataMat,2)
#kMeans_my.distEclud(dataMat[0],dataMat[1])


### k-均值聚类算法
def kMeans(dataSet,k,distMeas=distEclud,createCent = randCent):
    m = shape(dataSet)[0]    # 获得行数m
    clusterAssment = mat(zeros((m,2)))   #初始化一个矩阵，用来记录簇索引和存储误差。
    centroids = createCent(dataSet,k)     #随机的得到一个质心矩阵簇。
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  #对每个点寻找最近的质心
            minDist= inf
            minIndex = -1
            for j in range(k):  #遍历质心簇，寻找最近质心
                distJI = distMeas(centroids[j,:],dataSet[i,:])  #计算数据点和质心的欧氏距离
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChanged =True
            clusterAssment[i,:] = minIndex, minDist**2
        print centroids
        for cent in range(k):  #更新质心位置。
                ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
                # print clusterAssment[:,0].A;
                #print clusterAssment[:,0].A==cent;
                print nonzero(clusterAssment[:,0].A==cent);
                print nonzero(clusterAssment[:,0].A==cent)[0];
                centroids[cent,:] = mean(ptsInClust,axis=0)
                print centroids[cent,:]
    return centroids,clusterAssment


reload(kMeans_my)
dataMat = mat(kMeans_my.loadDataSet('testSet.txt'))
# myCentroids, clusteAssing = kMeans_my.kMeans(dataMat, 4)
#kMeans(dataMat,4);


###二分K-均值聚类算法

def biKmeans(dataSet,k,distMeas=distEclud):
    m = shape(dataSet) [0]
    clusterAssment = mat(zeros((m,2)))
    centroid0 = mean(dataSet,axis=0).tolist()[0]      #tolist()生成list。    axis=0 为列
    centList = [centroid0]
    for j in range(m):                   # 按行
        clusterAssment[j,1] = distMeas(mat(centroid0),dataSet[j,:])**2  # 求距离

    ###对簇划分
    while (len(centList) < k):
        lowestSSE = inf
        for i in range(len(centList)):     # len(centList) <= k
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A == i)[0],:]    # 列[:,0] 每个簇所有点视为一个小数据集。 i 第i个簇 。  取出第i个簇的所有数据，返回行号，对应到数据集的行。
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster,2,distMeas)       # 对每个簇划为2，距离度量。   返回质心和簇划分（索引，距离）
            sseSplit = sum(splitClustAss[:, 1])                #误差
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:,0].A != i)[0],1])     #簇误差
            print "sseSplit, and notSplit:",sseSplit,sseNotSplit
            # 返回 centroidMat,splitClustAss
            ####实际划分簇操作
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:0].A==1)[0],0] = len(centList)           #编号为0 ， 1 的结果簇。
        bestClustAss[nonzero(bestClustAss[:,0].A==0)[0],0] = bestCentToSplit
        print 'the bestCentToSplit is:' , bestCentToSplit
        print 'the len of bestClustAss is:' , len(bestClustAss)
        centList[bestCentToSplit] = bestNewCents[0,:]          # 簇bestCentToSplit的质心坐标
        centList.append(bestNewCents[1,:])                     # 簇bestCentToSplit的质心坐标添加到质心矩阵
        clusterAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:] = bestClustAss    # clusterAssment的行坐标更新为splitClustAss某簇的行坐标。
    return mat(centList), clusterAssment      #返回质心坐标，簇的行

reload(kMeans_my)
dataMat3 = mat(kMeans_my.loadDataSet('testSet2.txt'))
centList, myNewAssments = kMeans_my.biKmeans(dataMat3,3)
# # centList
# ###雅虎提供API，给定地址返回地址对应的经度纬度。
# import urllib
# import json
# ###对一个地址进行地理编码
# def geoGrab(stAddress, city):      #从雅虎返回一个字典
#     apiStem = 'http://where.yahooapis.com/geocode?'  #create a dict and constants for the goecoder
#     params = {}      #创建字典，为字典设置值。
#     params['flags'] = 'J'#JSON return type
#     params['appid'] = 'aaa0VN6k'
#     params['location'] = '%s %s' % (stAddress, city)
#     url_params = urllib.urlencode(params)       #字典转换为字符串。
#     yahooApi = apiStem + url_params      #print url_params
#     print yahooApi
#     c=urllib.urlopen(yahooApi)     #打开URL读取，URL传递字符串
#     return json.loads(c.read())    #将json格式解码为字典。
#
# from time import sleep
# def massPlaceFind(fileName):      #封装信息，并保存到文件。
#     fw = open('places.txt', 'w')  #打开一个以tab分隔的文本文件
#     for line in open(fileName).readlines():
#         line = line.strip()
#         lineArr = line.split('\t')
#         retDict = geoGrab(lineArr[1], lineArr[2])     #获取第2,3列结果
#         if retDict['ResultSet']['Error'] == 0:        #输出字典看有没有错误
#             lat = float(retDict['ResultSet']['Results'][0]['latitude'])   #若无错误，则读取经纬度。
#             lng = float(retDict['ResultSet']['Results'][0]['longitude'])
#             print "%s\t%f\t%f" % (lineArr[0], lat, lng)
#             fw.write('%s\t%f\t%f\n' % (line, lat, lng))    #添加到原来对应的行，同时写到新文件中。
#         else: print "error fetching"
#         sleep(1)      #休眠，防止频繁-调用。
#     fw.close()
# #import kMeans_my
# #geoResults = kMeans_my.geoGrab('1 VA Center','Augusta,ME')
# #geoResults
#
#
# #####对地理坐标进行聚类
# ###球面距离计算
# def distSLC(vecA, vecB):    #球面余弦定理
#     a = sin(vecA[0,1]*pi/180) * sin(vecB[0,1]*pi/180)       #pi/180转换为弧度 ，pi  ,numpy
#     b = cos(vecA[0,1]*pi/180) * cos(vecB[0,1]*pi/180) * \
#                       cos(pi * (vecB[0,0]-vecA[0,0]) /180)
#     return arccos(a + b)*6371.0
#
# ####簇绘图函数
# import matplotlib
# import matplotlib.pyplot as plt
# def clusterClubs(numClust=5):   #希望得到簇数目为5
#     datList = []               # 初始化，创建新列表
#     #####将文本文件的解析、聚类及画图都封装在一起
#     ##文件解析
#     for line in open('places.txt').readlines():     #对于读取文件的行，for循环。
#         lineArr = line.split('\t')
#         datList.append([float(lineArr[4]), float(lineArr[3])])   #获取文本第5,4列；这两列分别对应着经度和纬度。并添加到创建的新列表datList中。
#     dataMat = mat(datList)       #将基于经纬度创建的列表datList矩阵化。
#     ##聚类
#     myCentroids, clustAssing = biKmeans(dataMat, numClust, distMeas=distSLC)   #调用Kmeans函数，并使用球面余弦定理计算距离，返回myCentroids, clustAssing。
#     fig = plt.figure()  #可视化簇和簇质心。
#     ####为了画出这幅图，首先创建一幅画，一个矩形
#     rect = [0.1, 0.1, 0.8, 0.8]   #创建矩形。
#     scatterMarkers = ['s', 'o', '^', '8', 'p', \
#                       'd', 'v', 'h', '>', '<']     #使用唯一标记来标识每个簇。
#     axprops = dict(xticks=[], yticks=[])
#     ax0 = fig.add_axes(rect, label='ax0', **axprops)    #绘制一幅图，图0
#     imgP = plt.imread('Portland.png')    #调用 imread 函数，基于一幅图像，来创建矩阵。
#     ax0.imshow(imgP)              #调用imshow ，绘制（基于图像创建）矩阵的图。
#     ax1 = fig.add_axes(rect, label='ax1', frameon=False)    #绘制衣服新图，图1。 作用：使用两套坐标系统（不做任何偏移或缩放）。
#     ###遍历每个簇，把它画出来。
#     for i in range(numClust):     # 簇号循环。
#         ptsInCurrCluster = dataMat[nonzero(clustAssing[:, 0].A == i)[0], :]   #挑选出该簇所有点。
#         markerStyle = scatterMarkers[i % len(scatterMarkers)]      #从前面创建的标记列表中获得标记。使用索引i % len(scatterMarkers)选择标记形状。 作用：更多的图可以使用这些标记形状。
#         ax1.scatter(ptsInCurrCluster[:, 0].flatten().A[0], ptsInCurrCluster[:, 1].flatten().A[0], marker=markerStyle,s=90)
#         #每个簇的所有点ptsInCurrCluster，根据标记画出图形。
#     ax1.scatter(myCentroids[:, 0].flatten().A[0], myCentroids[:, 1].flatten().A[0], marker='+', s=300)    #使用 + 标记来表示簇中心，并在图中显示。
#     plt.show()
#
