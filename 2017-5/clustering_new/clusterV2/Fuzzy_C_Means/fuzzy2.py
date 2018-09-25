# # -*- coding: utf-8 -*-

import random
import math


# 用于初始化隶属度矩阵U
global MAX
MAX = 10000.0
# 用于结束条件
global Epsilon
Epsilon = 0.00000001

data=[]     #数据集
clust = []   #分类结果标签集，0,1,2



#按行读入，每行去除“，\n”，每行的特征数据转化为float并插入alist；
#alist插入data。
def import_data(path):   # 加载数据
    f = open(path)
    for i in f:
        row=i.replace("\n",',')
        row = row.strip()
        row = row.split(",")
        # row = row.strip("\n")
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
    # print("------data------")
    # print(data)
    # print("-----clust------")
    # print(clust)
    print("......加载数据完毕")
    return data,clust     #返回每条数据特征data，每条数据分类标签cluster



def randomise(data):   # 随机化数据，记录随机化后的数据
    length=len(data)  # 数据条数
    order_list = list(range(length))   # 数据条数长度range 的列表
    random.shuffle(order_list)       # 打乱range顺序
    ran_data=[[] for i in range(length)]  #新建length个空列表，记录 随机数据
    for i in range(length):   # 最终得到的随机数据
        ran_data[i]=data[order_list[i]]
    # print(ran_data)
    return ran_data,order_list


#返回数据原始顺序
def ori_order(data,order_list):  #将ran_data()返回的order_list列表作为参数
    # order_list = list(range(0, len(data)))
    length = len(order_list)
    ori_data=[[] for i in range(0,length)]
    for i in range(length):
        ori_data[i]=data[i]
    return ori_data



def print_mat(alist):      #打印矩阵
    for i in range(0,len(alist)):
        return alist[i]

# 归一化（保证每行和为1）的随机数放到cur列表 ， cur再放到 Uij列表作为隶属度。
#随机数的个数 clust_num
def init_Uij(data,clust_num):
    global  MAX    #全局变量
    Uij=[]   #隶属度矩阵 每行和为1
    length=len(data)
    for i in range(0,length):
        cur=[]
        rand_sum=0.0    #随机数和初始化为0
        for j in range(0,clust_num):
            rand_num=random.randint(1,int(MAX))   #生成随机数
            cur.append(rand_num)      #随机数放在 cur列表
            rand_sum+=rand_num        #随机数累加
        for j in range(0,clust_num):   #随机数归一化 放在cur列表
            cur[j]=cur[j]/rand_sum
        Uij.append(cur)    #归一化后的随机数cur列表 放到Uij 中
    return Uij
    # print("==UIJ==")
    # print(Uij)



#计算两点间距离 放在 dist列表        闵可夫斯基距离
def distance(point,cent):
    if len(point)!=len(cent):
        return -1
    rand_num=0.0
    for i in range(0,len(point)):   # 距离累加，所有点和中心点cent的距离
        rand_num+=abs(point[i]-cent[i])**2
    dist=math.sqrt(rand_num)
    return dist


# 当U矩阵随着连续迭代停止变化时，触发结束
def end(Uij,U0):    # 定义结束条件
    global Epsilon
    for i in range(0,len(Uij)):
        for j in range(0,len(Uij[0])):
            if abs(Uij[i][j]-U0[i][j]) > Epsilon:
                return False
    return True

#聚类结束时，模糊化 Uij，使每个样本的隶属度最大的为1，其余为0.
def norm_Uij(Uij):    # 模糊化隶属度
    for i in range(0,len(Uij)):
        max_num=max(Uij[i])   #找出最大的隶属度
        for j in range(0,len(Uij[0])):
            if Uij[i][j]!=max_num:
                Uij[i][j]=0
            else:
                Uij[i][j]=1
    return Uij






# if __name__ == '__main__':
#     # 加载数据
#     path="test.txt"
#     data, cluster_location = import_data(path)
#     print("---randomise:ran_data,order_list------")
#     print(randomise(data))
#     print("---ori_order:ran_data,ori_data------")
#     print(ori_order(data,randomise(data)))

