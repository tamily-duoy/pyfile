#!/usr/bin/python
# -*- coding:utf-8 -*-

def select_sort(a):
    # 选择排序
    for i in range(0, len(a)):
        pos = i
        for j in range(i + 1, len(a)):
            if a[pos] > a[j]:
                pos = j
        a[pos], a[i] = a[i], a[pos]
    return a

if __name__=='__main__':
    a=[4,3,1,7]
    c=select_sort(a)
    print(c)