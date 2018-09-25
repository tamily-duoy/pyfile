#encoding:utf-8


"""Given an array of integers, 
return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice. """
"""example:
 Given nums = [2, 7, 11, 15], target = 9,
 Because nums[0] + nums[1] = 2 + 7 = 9,
 return [0, 1]."""

#数据排序；
# 两个索引：从0开始、从最大开始；
##------------------------------------------
# 当值索引1<索引2 ：
    #如果，和与目标值相等，停止
    #如果，和与目标值不等，索引1加一，索引2减一
#当索引1=索引2,：
    #返回(-1, -1)
#否则：
    # 结果1=索引1的值；
    #结果二=索引2的值。
    #如果结果2=！结果1：
         #返回---
    #否则：
        #返回
def twoSum(self, num, target):
    tmp_num = num[:]
    tmp_num.sort()
    index1 = 0
    index2 = len(tmp_num) - 1
    while index1 < index2:
        tmp_target = tmp_num[index1] + tmp_num[index2]
        if tmp_target == target:
            break
        elif tmp_target > target:
            index2 -= 1
        else:
            index1 += 1
    if index1 == index2:
        return (-1, -1)
    else:
        ans1 = num.index(tmp_num[index1])
        ans2 = num.index(tmp_num[index2])
        if ans2 != ans1:
            # not zero based
            return (min(ans1, ans2) + 1, max(ans1, ans2) + 1)
        else:
            ans2 = num[ans1 + 1:].index(tmp_num[index2])
            return (ans1 + 1, ans1 + 1 + ans2 + 1)