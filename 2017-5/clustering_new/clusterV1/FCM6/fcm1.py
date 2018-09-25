# -*- coding: utf-8 -*-

import copy
import random
import pylab
import math

MAX=1e100

#初始化 样本点、标签、簇数、隶属度
class Point:
    __slots__=["x","y","clust","uij"]   #绑定属性：特征、标签、簇、隶属度
    def __init__(self,clust_num,x=0,y=0,clust=0):   #初始化 特征、标签、簇、隶属度（个数=簇数）
        self.x=x
        self.y=y
        self.clust=clust
        self.uij=[0.0 for i in range(clust_num)]


#生成点
def point2(point_num,r,clust_cent_num):
    points=[Point(clust_cent_num) for i in range(2*point_num)]
    count=0
    for point in points:
        count+=1
        R=random.random()*r
        angle=random.random()*2*math.pi
        point.x=R.math.cos(angle)
        point.y=R.math.sin(angle)
        if count==point_num-1:
            break
    for i in range(point_num,2*point_num):
        points[i].x=2*r*random.random()-r
        points[i].y=2*r*random()-r


    return points

#计算 两点间距离
def Distance(pointA, pointB):
    distance=(pointA.x - pointB.x) **2 + (pointA.y - pointB.y) **2
    return distance


#获得 簇中心
def cent(point,clust_group):
    min_index=point.clust   #点的group(clust)属性
    min_distance=MAX
    for index,cent in enumerate(clust_group):   #计算簇内 每个点到中心点的距离
        distance=Distance(point,cent)
        if (distance<min_distance):
            min_index=index
            min_distance=distance
    return (min_index,min_distance)


#每个簇的点 计算簇中所有点和中心点的距离
def kmean(point,cent_clust):
    cent_clust[0]=copy.copy(random.choice(point))  #簇中心
    distance_clust=[0.0 for i in range(len(point))]  #初始化簇的距离
    sum=0.0
    for i in range(1,len(cent_clust)):   # 簇 i
        for j,poin in enumerate(point):
            distance_clust[j]=cent(poin,cent_clust[:i])[1]
            sum+=distance_clust[j]
        sum*=random.random()
        for j,distance in enumerate(distance_clust):
            sum-=distance
            if sum<0:
                distance_clust[i]=copy.copy(point[j])
                break
    return




def get_uiji(poin,cent_clust,w):
    distance2=[Distance(poin,cent_clust[index]) for index in range(len(cent_clust))]
    for centindex,uiji in enumerate(poin.clust):
        sum=0.0
        coincide=[False,0]
        for index, distance in enumerate(distance2):
            if distance==0:
                coincide[0]=True
                coincide[1]=index
                break
            sum+=pow(float(distance2[centindex]/distance), 1.0/(w-1.0))
        if coincide[0]:
            if coincide[1]==centindex:
                poin.uij[centindex]=1.0
            else:
                poin.uij[centindex]=0.0
        else:
            poin.uij[centindex]=1.0/sum





def fuzzy_cmeans(point,cent_num,w):
    cent_clust=[Point(cent_num) for i in range(cent_num)]
    kmean(point,cent_clust)
    cent_trace=[[cent] for cent in cent_clust]
    tolerableError=1.0
    curError=MAX
    while curError>=tolerableError:
        for poin in point:
            get_uiji(poin,cent_clust,w)
        cur_cent_clust=[Point(cent_num) for i in range(cent_num)]
        for centindex,cent in enumerate(cent_clust):
            up_sum_x=0.0
            up_sum_y=0.0
            lower_sum=0.0
            for poin in point:
                uijw=pow(poin.uij[centindex],w)
                up_sum_x+=poin.x*uijw
                up_sum_y+=poin.y*uijw
                lower_sum+=uijw
            cent.x=up_sum_x/lower_sum
            cent.y=up_sum_y/lower_sum
        #更新簇中心的轨迹
        curError=0.0
        for index,tracei in enumerate(cent_trace):
            tracei.append(cur_cent_clust[index])
            curError+=Distance(tracei[-1],tracei[-2])
            cent_clust[index]=copy.copy(cur_cent_clust[index])
    for poin in point:
        max_index=0
        max_uij=0.0
        for index,uiji in enumerate(poin.uij):
            if uiji>max_uij:
                max_uij=uiji
                max_index=index
        poin.clust=max_index
    return cent_clust,cent_trace



def show(point,cent_trace):
    colorlist=['or', 'og', 'ob', 'oc', 'om', 'oy', 'ok']
    pylab.figure(figsize=(9,9),dpi=80)
    for poin in point:
        color=''
        if poin.clust>=len(colorlist):
            color=colorlist[-1]
        else:
            color=colorlist[poin.clust]
        pylab.plot(poin.x,poin.y,color)
    for tracei in cent_trace:
        pylab.plot([cent.x for cent in tracei],[cent.y for cent in tracei],'k')
    pylab.show()


def main():
    cent_num=5
    point_num=2000
    r=10
    w=2
    point=point2(point_num,r,cent_num)
    k,cent_trace=fuzzy_cmeans(point,cent_num,w)
    show(point,cent_trace)
main()









