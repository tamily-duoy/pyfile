# # -*- coding: utf-8 -*-

from cluster.Fuzzy_C_Means.fuzzy2 import *
# from cluster.clustering_new.Fuzzy_C_Means.fuzzy2 import *
import copy

#计算聚类中心 ，返回归一化的隶属度矩阵Uij。
#clust_num:簇数   隶属度因子：m
def fuzzy(data,clust_num,m):
    Uij=init_Uij(data,clust_num)   ## 初始化隶属度矩阵Uij
    while (True):   #  循环更新U
        U0=copy.deepcopy(Uij)    #创建副本，以检查结束条件
        C=[]     #计算聚类中心
        for i in range(0,clust_num):
            cur_cent=[]
            for j in range(0,len(data[0])):
                rand_num=0.0
                rand_num_sum=0.0
                for k in range(0,len(data)):
                    rand_num+=(Uij[k][j]**m)*data[k][j]  #分子--
                    rand_num_sum+=(Uij[k][j]**m)     #分母
                cur_cent.append(rand_num/rand_num_sum)    #第i列聚类中心
            C.append(cur_cent)      #第j列所有聚类中心 放到C
        dist_mat=[]   #距离向量
        for i in range(0,len(data)):
            cur=[]
            for j in range(0,clust_num):
                cur.append(distance(data[i],C[j]))
            dist_mat.append((cur))

        for j in range(0,clust_num):    #更新Uij
            for i in range(0,len(data)):
                rand_num=0.0
                for k in range(0,clust_num):
                    rand_num+=(dist_mat[i][j]/dist_mat[i][k])**(2/(m-1))  #分母
                Uij[i][j]=1/rand_num
        if end(Uij,U0):
            print("---end---")
            break
    print("-----Uij------")
    Uij=norm_Uij(Uij)
    return Uij






