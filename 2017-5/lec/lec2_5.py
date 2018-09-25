#!/usr/bin/python
# -*- coding:utf-8 -*-

#There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#例1    nums1 = [1, 3]    nums2 = [2]
# The median is 2.0
#例2  nums1 = [1, 2]  nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5




#对于一个长度为n的已排序数列a，若n为奇数，中位数为a[n / 2 + 1] ,
    # 若n为偶数，则中位数(a[n / 2] + a[n / 2 + 1]) / 2
    # 如果我们可以在两个数列中求出第K小的元素，便可以解决该问题
    # 不妨设数列A元素个数为n，数列B元素个数为m，各自升序排序，求第k小元素
    # 取A[k / 2] B[k / 2] 比较，
    # 如果 A[k / 2] > B[k / 2] 那么，所求的元素必然不在B的前k / 2个元素中(证明反证法)
    # 反之，必然不在A的前k / 2个元素中，于是我们可以将A或B数列的前k / 2元素删去，求剩下两个数列的
    # k - k / 2小元素，于是得到了数据规模变小的同类问题，递归解决
    # 如果 k / 2 大于某数列个数，所求元素必然不在另一数列的前k / 2个元素中，同上操作就好



#两种思路：
# 1. 直接 merge 两个数组，然后求中位数，能过，不过复杂度是 O(n + m)。
# 2. 用二分的思路去做，这不好想，还要考虑到奇偶。可以转化思维，去求两个有序数组中的第 K 大数，这样就比较好想了。


class Solution(object):
    def getMedian(self, nums):    #得到中位数
        size = len(nums)
        if size == 0:
            return [0, 0]
        if size % 2 == 1:   #判断 长度为 奇数
            return [nums[size // 2], size // 2]     # //整除
        return [(float(nums[size // 2 - 1] + nums[size // 2])) / 2, size // 2]   # nums[]s索引


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size1 = len(nums1)
        size2 = len(nums2)
        if size1 < size2:
            return self.findMedianSortedArrays(nums2, nums1)
        m1 = self.getMedian(nums1)
        m2 = self.getMedian(nums2)
        if size2 == 0:  #若num2没有元素:
            return m1[0]
        if size2 == 1:   #若num2只有一个元素：
            if size1 == 1:
                return (float(nums1[0] + nums2[0])) / 2   #两列表都只有一个元素，中位数=(num1 +num2)/2
            if size1 % 2 == 0:  #此时，num1是偶数时
                if nums2[0] < nums1[size1 // 2 - 1]:
                    return nums1[size1 // 2 - 1]
                if nums2[0] > nums1[size1 // 2]:
                    return nums1[size1 // 2]
                else:
                    return nums2[0]
            else:   #num1是奇数时
                if nums2[0] < nums1[size1 // 2 - 1]:
                    return (float(nums1[size1 // 2 - 1] + nums1[size1 // 2])) / 2
                if nums2[0] > nums1[size1 // 2 + 1]:
                    return (float(nums1[size1 // 2] + nums1[size1 // 2 + 1])) / 2
                else:
                    return (float(nums2[0] + nums1[size1 // 2])) / 2
        if size2 % 2 == 0:  #若num2有偶数元素
            if size1 % 2 == 0:
                if nums2[size2 // 2 - 1] < nums1[size1 // 2 - 1] and nums2[size2 // 2] > nums1[size1 // 2]:
                    return m1[0]
                if nums1[size1 // 2 - 1] < nums2[size2 // 2 - 1] and nums1[size1 // 2] > nums2[size2 // 2]:
                    return m2[0]
        if m1[0] < m2[0]:
            return self.findMedianSortedArrays(nums1[m2[1]:], nums2[:size2 - m2[1]])
        if m1[0] > m2[0]:
            return self.findMedianSortedArrays(nums1[:size1 - m2[1]], nums2[m2[1]:])
        else:
            return m1[0]

if __name__ == '__main__':
    nums = [1, 2]
    nums1=[1, 2]
    nums2 =[3, 4]
    solution=Solution()
    print(solution.getMedian(nums))
    print(solution.findMedianSortedArrays(nums1, nums2))



    # Time:  O(log(min(m, n)))
    # Space: O(1)

    # There are two sorted arrays nums1 and nums2 of size m and n respectively.
    # Find the median of the two sorted arrays.
    # The overall run time complexity should be O(log (m+n)).

# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         len1, len2 = len(nums1), len(nums2)
#         if (len1 + len2) % 2 == 1:
#             return self.getKth(nums1, nums2, (len1 + len2) / 2 + 1)
#         else:
#             return (self.getKth(nums1, nums2, (len1 + len2) / 2) + \
#                     self.getKth(nums1, nums2, (len1 + len2) / 2 + 1)) * 0.5
#
#     def getKth(self, A, B, k):
#         m, n = len(A), len(B)
#         if m > n:
#             return self.getKth(B, A, k)
#
#         left, right = 0, m
#         while left < right:
#             mid = left + (right - left) / 2
#             if 0 <= k - 1 - mid < n and A[mid] >= B[k - 1 - mid]:
#                 right = mid
#             else:
#                 left = mid + 1
#
#         Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
#         Bj = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")
#
#         return max(Ai_minus_1, Bj)
#
#
# # Time:  O(log(max(m, n)) * log(max_val - min_val))
# # Space: O(1)
# # Generic solution.
# class Solution_Generic(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         len1, len2 = len(nums1), len(nums2)
#         if (len1 + len2) % 2 == 1:
#             return self.getKth([nums1, nums2], (len1 + len2) / 2 + 1)
#         else:
#             return (self.getKth([nums1, nums2], (len1 + len2) / 2) + \
#                     self.getKth([nums1, nums2], (len1 + len2) / 2 + 1)) * 0.5
#
#     def getKth(self, arrays, k):
#         def binary_search(array, left, right, target, compare):
#             while left <= right:
#                 mid = left + (right - left) / 2
#                 if compare(array, mid, target):
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             return left
#
#         def match(arrays, num, target):
#             res = 0
#             for array in arrays:
#                 if array:
#                     res += len(array) - binary_search(array, 0, len(array) - 1, num, \
#                                                       lambda array, x, y: array[x] > y)
#             return res < target
#
#         left, right = float("inf"), float("-inf")
#         for array in arrays:
#             if array:
#                 left = min(left, array[0])
#                 right = max(right, array[-1])
#
#         return binary_search(arrays, left, right, k, match)
#
#
# if __name__ == "__main__":
#     print ( Solution().findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6]))
#     print (Solution().findMedianSortedArrays([1, 3, 5], [2, 4, 6]))












# class Solution:
#     def findKthSortedArrays(self, A, B, k):
#         if len(A) < len(B):
#             tmp = A
#             A = B
#             B = tmp
#         if len(B) == 0:
#             return A[k - 1]
#         if k == 1:
#             return min(A[0], B[0])
#
#         pb = min(k / 2, len(B))
#         pa = k - pb
#         if A[pa - 1] > B[pb - 1]:
#             return self.findKthSortedArrays(A, B[pb:], k - pb)
#         elif A[pa - 1] < B[pb - 1]:
#             return self.findKthSortedArrays(A[pa:], B, k - pa)
#         else:
#             return A[pa - 1]
#
#             # @return a float
#
#     def findMedianSortedArrays(self, A, B):
#         if (len(A) + len(B)) % 2 == 1:
#             return self.findKthSortedArrays(A, B, (len(A) + len(B)) / 2 + 1)
#         else:
#             return (self.findKthSortedArrays(A, B, (len(A) + len(B)) / 2) +
#                     self.findKthSortedArrays(A, B, (len(A) + len(B)) / 2 + 1)) / 2.0