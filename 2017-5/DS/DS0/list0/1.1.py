#!/usr/bin/python
# -*- coding:utf-8 -*-
#Node实现
class Node():
    __slots__=['_item','_next']    #限定Node实例的属性
    def __init__(self,item):  #创建类实例
        self._item=item
        self._next=None     #Node的指针部分默认指向None
    def getItem(self):
        return self._item
    def getNext(self):
        return self._next
    def setItem(self,newitem):
        self._item=newitem
    def setNext(self,newnext):
        self._next=newnext

# class Node:
#     '''
#     data: 节点保存的数据
#     _next: 保存下一个节点对象
#     '''
#     def __init__(self, data, pnext=None):
#         self.data = data
#         self._next = pnext
#
#     def __repr__(self):
#         '''
#         用来定义Node的字符输出，
#         print为输出data
#         '''
#         return str(self.data)