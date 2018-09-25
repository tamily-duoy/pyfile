#!/usr/bin/python
# -*- coding:utf-8 -*-

class MyQueue():
    def __init__(self, value=None):
        self.value = value
        # 前驱
        # self.before = None
        # 后继
        self.behind = None

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return 'None'


def create_queue():
    """仅有队头"""
    return MyQueue()


def last(queue):
    if isinstance(queue, MyQueue):
        if queue.behind is not None:
            return last(queue.behind)
        else:
            return queue


def push(queue, ele):   #输入
    if isinstance(queue, MyQueue):
        last_queue = last(queue)
        new_queue = MyQueue(ele)
        last_queue.behind = new_queue


def pop(queue):     #输出
    if queue.behind is not None:
        get_queue = queue.behind
        queue.behind = queue.behind.behind
        return get_queue
    else:
        print('队列里已经没有元素了')

def print_queue(queue):
    print(queue)
    if queue.behind is not None:
        print_queue(queue.behind)


class Queue:
    """模拟队列"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#测试代码
q = Queue()
q.isEmpty()

q.enqueue('dog')
q.enqueue(4)
q = Queue()
q.isEmpty()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)