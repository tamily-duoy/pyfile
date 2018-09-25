# # -*- coding: utf-8 -*-

import random
import math



global MAX
MAX = 10000.0
global Epsilon
Epsilon = 0.00000001

data=[]     #数据集
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
    return data,clust     #返回每条数据特征data，每条数据分类标签cluster



def randomise(data):   # 随机化数据，记录随机化后的数据
    length=len(data)
    order_list = list(range(length))
    random.shuffle(order_list)       # 打乱range顺序
    ran_data=[[] for i in range(length)]
    for i in range(length):
        ran_data[i]=data[order_list[i]]
    return ran_data,order_list


#返回数据原始顺序
def ori_order(data,order_list):
    length = len(order_list)
    ori_data=[[] for i in range(0,length)]
    for i in range(length):
        ori_data[i]=data[i]
    return ori_data



def print_mat(alist):      #打印矩阵
    for i in range(0,len(alist)):
        return alist[i]

# 归一化（保证每行和为1）的随机数放到cur列表 ， cur再放到 Uij列表作为隶属度。

def init_Uij(data,clust_num):
    global  MAX
    Uij=[]   #隶属度矩阵 每行和为1
    length=len(data)
    for i in range(0,length):
        cur=[]
        rand_sum=0.0
        for j in range(0,clust_num):
            rand_num=random.randint(1,int(MAX))
            cur.append(rand_num)
            rand_sum+=rand_num
        for j in range(0,clust_num):
            cur[j]=cur[j]/rand_sum
        Uij.append(cur)    #归一化后的随机数cur列表 放到Uij 中
    return Uij



#计算两点间距离 放在 dist列表        闵可夫斯基距离
def distance(point,cent):
    if len(point)!=len(cent):
        return -1
    rand_num=0.0
    for i in range(0,len(point)):
        rand_num+=abs(point[i]-cent[i])**2
    dist=math.sqrt(rand_num)
    return dist



def end(Uij,U0):    # 定义结束条件
    global Epsilon
    for i in range(0,len(Uij)):
        for j in range(0,len(Uij[0])):
            if abs(Uij[i][j]-U0[i][j]) > Epsilon:
                return False
    return True

#聚类结束时，模糊化 Uij，使每个样本的隶属度最大的为1，其余为0.
def norm_Uij(Uij):
    for i in range(0,len(Uij)):
        max_num=max(Uij[i])
        for j in range(0,len(Uij[0])):
            if Uij[i][j]!=max_num:
                Uij[i][j]=0
            else:
                Uij[i][j]=1
    return Uij





