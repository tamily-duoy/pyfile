#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

# 2.1  array函数
a=([1,2],[3,4])
np.array(a)

#  array([[1, 2],
#        [3, 4]])


#2.2   arange函数：初始值、终值、步长
np.arange(3,5,0.5)

#array([ 3. ,  3.5,  4. ,  4.5])


# 2.3  linspace函数:开始值、终值和元素个数
# 可以通过endpoint:指定是否包括终值，缺省设置是包括终值
np.linspace(3,5,5)

#array([ 3. ,  3.5,  4. ,  4.5,  5. ])


#2.4   logspace能创建等比数列：  10^0=1到10^=100的共20个元素的等比数列
np.logspace(1,2,20)

#2.5  使用frombuffer, fromstring, fromfile等函数
# 可以从字节序列创建数组
s='abcdefg'
np.fromstring(s,dtype=np.int8)

#array([ 97,  98,  99, 100, 101, 102, 103], dtype=int8)


#2.6   fromfunction函数的第一个参数为计算每个数组元素的函数
# 第二个参数为数组的大小(shape)
#因为它支持多维数组，所以第二个参数必须是一个序列
def func(i,j):
    return (i+1)*(j+1)
a=np.fromfunction(func,(3,2))    # i行，j列

# array([[ 1.,  2.],
#        [ 2.,  4.],
#        [ 3.,  6.]])


