#!/usr/bin/python
# -*- coding:utf-8 -*-

#定义堆栈
class my_stack(object):
    def __init__(self, value):
        self.value = value
        # 前驱
        self.before = None
        # 后继
        self.behind = None

    def __str__(self):
        return str(self.value)

#定义栈顶
def top(stack):
    if isinstance(stack, my_stack):
        if stack.behind is not None:
            return top(stack.behind)
        else:
            return stack

# 定义输入
def push(stack, ele):
    push_ele = my_stack(ele)
    if isinstance(stack, my_stack):
        stack_top = top(stack)
        push_ele.before = stack_top
        push_ele.before.behind = push_ele
    else:
        raise Exception('不要乱扔东西进来好么')

#定义输出
def pop(stack):
    if isinstance(stack, my_stack):
        stack_top = top(stack)
        if stack_top.before is not None:
            stack_top.before.behind = None
            stack_top.behind = None
            return stack_top
        else:
            print('已经是栈顶了')


#python的list对象模拟栈的实现：
class Stack:
    """模拟栈"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):     #Python Package Index
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 创建一个栈对象，并加入操作方法：
s=Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())