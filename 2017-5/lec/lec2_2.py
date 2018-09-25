#!/usr/bin/python
# -*- coding:utf-8 -*-
#for example,
# Given sorted array nums = [1,1,1,2,2,3],
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
# It doesn't matter what you leave beyond the new length.
#跟定一个排好序的数组。修改这个数组使得每个数最多可以出现两次。返回去掉多余重复数组后的长度，当然将多余重复数放到数组后面并不影响。
#题目思路：
   # 利用两个下标，一个用来遍历数组，另外一个来记录新数组，用一个bool变量来记录是否这个数值已经访问过1次。时间复杂度O（n）。
class Solution(object):
    def removeDuplicates(self, nums):
        """:type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0 or size == 1:
            return size
        begin,i = 1,1
        tmp,visit = nums[0],False
        while i < size:
            if nums[i] == tmp:
                if not visit:
                    nums[begin] = tmp
                    begin += 1;visit = True
            else:
                tmp,visit = nums[i],False
                nums[begin] = tmp
                begin += 1
            i += 1
        return begin

if __name__ == "__main__":
    assert Solution().removeDuplicates([1, 1, 2]) == 2