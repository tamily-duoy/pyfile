# # -*- coding: utf-8 -*-

from clustering_new.Fuzzy_C_Means.fuzzy2 import *
import copy

def fuzzy(data,clust_num,m):
    Uij=init_Uij(data,clust_num)
    while (True):
        U0=copy.deepcopy(Uij)
        C=[]
        for i in range(0,clust_num):
            cur_cent=[]
            for j in range(0,len(data[0])):
                rand_num=0.0
                rand_num_sum=0.0
                for k in range(0,len(data)):
                    rand_num+=(Uij[k][j]**m)*data[k][j]
                    rand_num_sum+=(Uij[k][j]**m)
                cur_cent.append(rand_num/rand_num_sum)
            C.append(cur_cent)
        print(C)

        dist_mat=[]
        for i in range(0,len(data)):
            cur=[]
            for j in range(0,clust_num):
                cur.append(distance(data[i],C[j]))
            dist_mat.append((cur))

        for j in range(0,clust_num):
            for i in range(0,len(data)):
                rand_num=0.0
                for k in range(0,clust_num):
                    rand_num+=(dist_mat[i][j]/dist_mat[i][k])**(2/(m-1))
                Uij[i][j]=1/rand_num
        if end(Uij,U0):
            print("---end---")
            break
    print("-----Uij------")
    Uij=norm_Uij(Uij)
    return Uij


if __name__=="__main__":
    path="test.txt"
    data, cluster_location = import_data(path)
    print("---randomise:ran_data,order_list------")
    print(randomise(data))
    print("---ori_order:ran_data,ori_data------")
    print(ori_order(data,randomise(data)))



