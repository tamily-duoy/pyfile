#!/usr/bin/python
# -*- coding:utf-8 -*-

def heapSort(a):
    # 冒泡排序: 小->大
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

if __name__=='__main__':
    a=[11, 1, 6, 9, 8, 5]
    c=heapSort(a)
    print(c)