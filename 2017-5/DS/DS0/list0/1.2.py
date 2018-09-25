#!/usr/bin/python
# -*- coding:utf-8 -*-
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



#1.2 SinglelinkedList
class SingleLinkedList():
    def __init__(self):
        self._head=None    #初始化链表为空表
        self._size=0


#1.3 检测链表是否为空
def isEmpty(self):
    return self._head==None


#1.4 add在链表前端添加元素
def add(self,item):
    temp=Node(item)
    temp.setNext(self._head)
    self._head=temp


#1.5  append在链表尾部添加元素
def append(self,item):
    temp=Node(item)  #要插入的元素
    if self.isEmpty():
        self._head=temp   #若为空表，将添加的元素设为第一个元素
    else:
        current=self._head
        while current.getNext()!=None:
            current=current.getNext()   #遍历链表
        current.setNext(temp)   #此时current为链表最后的元素

#1.6  search检索元素是否在链表中
def search(self,item):
    current=self._head
    founditem=False
    while current!=None and not founditem:
        if current.getItem()==item:
            founditem=True
        else:
            current=current.getNext()
    return founditem


# 1.7 index索引元素在链表中的位置
def index(self,item):
    current=self._head
    count=0
    found=None
    while current!=None and not found:
        count+=1
        if current.getItem()==item:
            found=True
        else:
            current=current.getNext()
    if found:
        return count
    else:
        raise ValueError('%s is not in linkedlist'%item)


# 1.8  remove删除链表中的某项元素
def remove(self,item):
    current=self._head
    pre=None
    while current!=None:
        if current.getItem()==item:
            if not pre:
                self._head=current.getNext()
            else:
                pre.setNext(current.getNext())
            break
        else:
            pre=current
            current=current.getNext()


# 1.9  insert链表中插入元素
# def insert(self,pos,item):
#     if posself.size():
#         self.append(item)
#     else:
#         temp=Node(item)
#         count=1
#         pre=None
#         current=self._head
#         while count
def insert(self,pos,item):
    if pos<=1:   #空链表，直接添加
        self.add(item)
    elif pos>self.size():  #插入位置>链表长度，直接插入
        self.append(item)
    else:    #插入位置在链表中
        temp=Node(item)
        count=1
        pre=None
        current=self._head
        while count<pos:
            count+=1
            pre=current
            current=current.getNext()
        pre.setNext(temp)
        temp.setNext(current)



#1.10
def size(self):
    current=self._head
    count=0
    while current!=None:
      count+=1
      current=current.getNext()
    return count
def travel(self):
  current=self._head
  while current!=None:
      print (current.getItem())
      current=current.getNext()


if __name__=='__main__':
    a=SingleLinkedList()
    for i in range(1,10):
        a.append(i)

    print (a.size())
    a.travel()
    print (a.search(6))
    print (a.index(5))
    a.remove(4)
    a.travel()
    a.insert(4,100)
    a.travel()