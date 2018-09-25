#!/usr/bin/python
# -*- coding:utf-8 -*-

def straightInsert(a):
# 直接插入排序: 小->大
    for i in range(1, len(a)):
        index = a[i]
        j = i - 1
        while j >= 0 and a[j] > index:
            a[j+1] = a[j]
            j -= 1
        a[j + 1] = index
    return a

if __name__=='__main__':
    a=[4,3,1,7]
    c=straightInsert(a)
    print(c)
