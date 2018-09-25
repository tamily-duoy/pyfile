#!/usr/bin/python
# -*- coding:utf-8 -*-
#Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
#去除重复元素，每个元素只出现一次，要求不增加新的数组空间实现，且新数组后面的部分不影响，返回值为新数组的长度
# 思路：采用两指针，一个指针i指向原数组需要判断的元素，一个指针j指向新数组新加入的元素。
# 由于是有序数组，因此只要判断原数组中的元素不同于新数组新加入的元素，
# 就将原数组的元素和新数组后一元素交换位置即可，没有重复元素就是和自身交换位置。

# class Solution(object):
#     def removeDuplicates(self, nums):
#         if len(nums)==0:
#             return 0
#         j=0
#         for i in range(1,len(nums)):
#             if nums[i]!=nums[j]:
#                 nums[j+1]=nums[i]
#                 j=j+1
#         return  j+1

#这道题类似实现C++ 中的去重操作，
# 大致思路：遍历一遍数组将所有重复元素取第一个依次放到数组的最前面，然后截取数组的前半段即可
# 具体实现：遍历数组，用start记录遇到的每次遇到第一个重复元素要调整到的位置：
# 这里start初值为1而不是0，因为新数组的第一个元素和旧数组是一样的，用keyValue记录遇到的重复元素，
# 遍历数组，每次遇到新的重复元素，则更新keyValue，然后将该元素放到start指示的位置上，然后start向后挪一位，
# 最后把原数组前半段没有重复元素的部分作为新数组（题目要求必须进行截取，否则WA），此时start的值就是新数组长度。
A=[1,1,2]
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A==[]: return 0
        start=1;keyValue=A[0];length=len(A)
        for i in range(length):
            if A[i]!=keyValue:
                keyValue=A[i]
                A[start]=A[i]
                start+=1
        A=A[:start]   #数组前半段
        return start
