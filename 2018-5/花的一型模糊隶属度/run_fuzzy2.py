# # -*- coding: utf-8 -*-

from clustering_new.clusterV2.Fuzzy_C_Means.fuzzy2 import *
import copy
import time

def fuzzy(data,clust_num,m):
    Uij=init_Uij(data,clust_num)   #调用函数，初始化隶属度
    while (True):
        U0=copy.deepcopy(Uij)    #深拷贝隶属度
        C=[]
        for i in range(0,clust_num):   #对于每个簇内部
            cur_cent=[]
            for j in range(0,len(data[0])):   #每个特征维度
                rand_num=0.0
                rand_num_sum=0.0
                for k in range(0,len(data)):
                    rand_num += (Uij[k][i] ** m) * data[k][j]
                    rand_num_sum += (Uij[k][i] ** m)
                cur_cent.append(rand_num/rand_num_sum)  #每个簇中心 的迭代公式，据公式
            C.append(cur_cent)
        print(C)    #簇中心

        dist_mat=[]
        for i in range(0,len(data)):
            cur=[]
            for j in range(0,clust_num):
                cur.append(distance(data[i],C[j]))
            dist_mat.append((cur))   #距离矩阵

        for j in range(0,clust_num):
            for i in range(0,len(data)):
                rand_num=0.0
                for k in range(0,clust_num):
                    rand_num+=(dist_mat[i][j]/dist_mat[i][k])**(2/(m-1))  #隶属度迭代公式 ，据公式
                Uij[i][j]=1/rand_num
        if end(Uij,U0):
            print("---end---")
            break    #迭代终止条件
    Uij=norm_Uij(Uij)
    return Uij   #返回隶属度


def checker_iris(final_location):
    right = 0.0
    for k in range(0, 3):
        checker = [0, 0, 0]
        # for i in range(0, 50):
        for i in range(0, 2):
            for j in range(0, len(final_location[0])):
                # if final_location[i + (50 * k)][j] == 1:
                if final_location[i + (2 * k)][j] == 1:
                    checker[j] += 1
        right += max(checker)
    answer = right / 6 * 100
    return "准确度：" + str(answer) + "%"



if __name__ == '__main__':
    # 加载数据
    data, cluster_location = import_data("test.txt")
    data,order = randomise(data)
    start = time.time()
    final_location = fuzzy(data, 2, 2)
    final_location = ori_order(final_location, order)
    # 准确度分析
    print(checker_iris(final_location))
    print("用时：{0}".format(time.time() - start))


