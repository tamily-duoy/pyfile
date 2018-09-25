import matplotlib.pyplot as plt

from numpy import *   #科学计算包
import operator       #运算符模块

def creatDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])  #创建数据集
    labels=['A','A','B','B']                          #创建标签
    return group,labels

plt.scatter(group,labels)
for group_i in group:
    for label,group_i in zip(labels,group):
        plt.annotate(label,
                 xy=(label,group_i),
                 xytext=(5,-5),
                 textcoords='offset points')

plt.title("w")
plt.xlabel("v")
plt.ylabel("m")
plt.show()
