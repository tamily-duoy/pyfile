# -*- coding: utf-8 -*-

import math
import random
import pylab
from matplotlib import pyplot as plt

MAX = 1e100

# class Point:
#     __slots__ = ["x", "y", "group", "uij"]  #绑定属性
#     def __init__(self, cent_num, x = 0, y = 0, group = 0):
#         self.x = x
#         self.y =  y
#         self.group = group
#         self.uij = [0.0 for i in range(cent_num)]      #初始化 隶属度
#
# #生成点
# def Points(point_num, r, cent_num):
#     points = [Point(cent_num) for i in range(2 * point_num)]
#     count = 0
#     for point in points:
#         count += 1
#         R = random.random() * r    #random.random()生成[0,1）的实数
#         angle = random.random() * 2 * math.pi
#         point.x = R * math.cos(angle)
#         point.y = R * math.sin(angle)
#         if count == point_num - 1:
#             break
#     for index in range(point_num, 2 * point_num):
#         points[index].x = 2 * r * random.random() - r
#         points[index].y = 2 * r * random.random() - r
#     return points



data=[]
clust = []
def import_data(path):   # 加载数据
    f = open(path)
    for i in f:
        row=i.replace("\n",',')
        row = row.strip()
        row = row.split(",")
        alist = []
        for j in range(0,len(row) - 2):
            alist.append(float(row[j]))
            j+=1
            if row[j] == "Iris-setosa":
                clust.append(0)
            elif row[j] == "Iris-versicolor":
                clust.append(1)
            elif row[j] == "Iris-virginica":
                clust.append(2)
        data.append(alist)
    print("......加载数据完毕")
    print(clust)
    return data,clust     #返回每条数据特征data，每条数据分类标签cluster


def show(data,clust):
    pylab.figure(figsize=(9, 9), dpi=80)
    for i in clust:
        # color=''
        if clust[i]==0:
            color='>r'
        elif clust[i]==1:
            color = 'og'
        else:
            color = 'xy'
        pylab.plot(data,clust,color)
    pylab.show()





def main():
    path = "test.txt"
    data, clust = import_data(path)
    show(data, clust)
    print(clust)


main()
