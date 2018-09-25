# # -*- coding: utf-8 -*-

import random
import math



global MAX
MAX = 10000.0
global Epsilon
Epsilon = 0.00000001

data=[]
clust = []


def import_data(path):
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
    print("------data------")
    print(data)
    print("-----clust------")
    print(clust)
    print("......加载数据完毕")
    return data,clust

def randomise(data):
    length=len(data)
    order_list = list(range(length))
    random.shuffle(order_list)
    ran_data=[[] for i in range(length)]
    for i in range(length):
        ran_data[i]=data[order_list[i]]
    print(ran_data)
    return order_list

def ori_order(data,order_list):
    length = len(order_list)
    ori_data=[[] for i in range(0,length)]
    for i in range(length):
        ori_data[i]=data[i]
    return ori_data

def print_mat(alist):
    for i in range(0,len(alist)):
        print(alist[i])

def init_Uij(data,clust_num):
    global  MAX
    Uij=[]
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
        Uij.append(cur)
    return Uij

def distance(point,cent):
    if len(point)!=len(cent):
        return -1
    rand_num=0.0
    for i in range(0,len(point)):
        rand_num+=abs(point[i]-cent[i])**2
    dist=math.sqrt(rand_num)
    return dist


def end(Uij,U0):
    global Epsilon
    for i in range(0,len(Uij)):
        for j in range(0,len(Uij[0])):
            if abs(Uij[i][j]-U0[i][j]) > Epsilon:
                return False
    return True


def nor_Uij(Uij):
    for i in range(0,len(Uij)):
        max_num=max(Uij[i])
        for j in range(0,len(Uij[0])):
            if Uij[i][j]!=max_num:
                Uij[i][j]=0
            else:
                Uij[i][j]=1
    return Uij







if __name__ == '__main__':
    path="test.txt"
    data, cluster_location = import_data(path)
    print("---randomise:ran_data,order_list------")
    print(randomise(data))
    print("---ori_order:ran_data,ori_data------")
    print(ori_order(data,randomise(data)))

