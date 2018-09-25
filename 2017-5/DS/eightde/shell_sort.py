#!/usr/bin/python
# -*- coding:utf-8 -*-

def shell_sort(a):
    # 希尔排序
    step = 2
    group = len(a)// step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < len(a):
                k = j - group
                key = a[j]
                while k >= 0:
                    if a[k] > key:
                        a[k + group] = a[k]
                        a[k] = key
                    k -= group
                j += group
        group //= step
    return a

if __name__=='__main__':
    a=[4,3,1,7]
    c=shell_sort(a)
    print(c)