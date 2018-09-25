#!/usr/bin/python
# -*- coding:utf-8 -*-

# 1.1  简单树
# myTree = ['a',   #root
#       ['b',  #left subtree
#        ['d' [], []],
#        ['e' [], []] ],
#       ['c',  #right subtree
#        ['f' [], []],
#        [] ]
#      ]

#1.2
myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
# print(myTree)
# print('left subtree = ', myTree[1])
# print('root = ', myTree[0])
# print('right subtree = ', myTree[2])

#1.3   定义函数
def BinaryTree(r):
    return [r, [], []]

#  1.4 以1.3为基础， Listing 1 显示了插入左子节点。
def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

# 1.5  右节点
def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root


#1.6 获取和设置根值的函数，以及获得左边或右边子树。
def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]

#1.7 完整的嵌套列表表示树。
def BinaryTree(r):    #定义树
    return [r, [], []]
def insertLeft(root, newBranch):  #插入左叶子
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root
def insertRight(root, newBranch): #右叶子
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root
#获得叶子的函数
def getRootVal(root):
    return root[0]
def setRootVal(root, newVal):
    root[0] = newVal
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]
r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
l = getLeftChild(r)
print(l)

setRootVal(l, 9)
print(r)
insertLeft(l, 11)
print(r)
print(getRightChild(getRightChild(r)))