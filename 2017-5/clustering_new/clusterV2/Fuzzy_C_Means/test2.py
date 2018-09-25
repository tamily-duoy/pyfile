# # -*- coding: utf-8 -*-

from cluster.Fuzzy_C_Means.fuzzy2 import *
import copy
import time

def num_to_list(num,n):
    alist=[]
    for i in range(n):
        alist.append(num)
    return alist

def fuzzy(data,clust_num,m):
    Uij=init_Uij(data,clust_num)   #调用函数，初始化隶属度,  簇数*1
    while (True):
        U0=copy.deepcopy(Uij)    #深拷贝隶属度
        C=[]
        for i in range(0, clust_num):   #对于每个簇内部，计算簇中心
            cur_cent = []
            for k in range(0, len(data)):  # 数据条数，每条数据 *隶属度，累加得到 簇中心
                rand_num = 0.0
                rand_num_sum = 0.0
                Uij[k] = Uij[k] ** m
                for j in range(0, len(data[0])):  # 每个特征维度
                    Uij[k]=num_to_list(Uij[k],len(data[0]))
                    rand_num +=Uij[k][j]* data[k][j]
                    rand_num_sum+=Uij[k][j]
                cur_cent.append(rand_num / rand_num_sum)  # 每个簇中心 的迭代公式，据公式
                C.append(cur_cent)
                print(C)  # 簇中心
                dist_mat = []
                for i in range(0, len(data)):
                    cur = []
                    for j in range(0, clust_num):
                        cur.append(distance(data[i], C[j]))
                    dist_mat.append((cur))  # 距离矩阵
                for j in range(0, clust_num):
                    for i in range(0, len(data)):
                        rand_num = 0.0
                        for k in range(0, clust_num):
                            rand_num += (dist_mat[i][j] / dist_mat[i][k]) ** (2 / (m - 1))  # 隶属度迭代公式 ，据公式
                        Uij[i][j] = 1 / rand_num
                if end(Uij, U0):
                    print("---end---")
                    break  # 迭代终止条件
            print("-----Uij------")
            Uij = norm_Uij(Uij)
            return Uij





if __name__ == '__main__':
    data, cluster_location = import_data("test.txt")
    data,order = randomise(data)
    start = time.time()
    final_location = fuzzy(data, 2, 2)