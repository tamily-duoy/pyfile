# # 简化路径
# # def simplePath(path):
# #     stack=[]
# #     result=""
# #     arr=path.split("/")
# #     list1=["",".",".."]
# #     if path==None:
# #         return 0
# #     if len(path)>4096:
# #         return 0
# #     for i in arr:
# #         if i not in list1:
# #             stack.append(i)
# #         if i=="..":
# #             stack.pop(-1)
# #     if stack==[]:
# #         return "/"
# #     for i in stack:
# #         result+="/"+i
# #     return result
# # a="/a/././b//../../c/"
# # c=simplePath(a)
# # print(c)
#
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         # 判断是否为空
#         if not strs:
#             return ''
#         # 在使用max和min的时候已经把字符串比较了一遍
#         # 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最小的字符串
#         s1 = min(strs)
#         # print("S1：####")
#         # print(s1)
#         # 当前列表的字符串中，每个字符串从第一个字母往后比较直至出现ASCII码 最大的字符串
#         s2 = max(strs)
#         # print("S2：###")
#         # print(s2)
#         # 使用枚举变量s1字符串的每个字母和下标
#         for i, c in enumerate(s1):
#             # 比较是否相同的字符串，不相同则使用下标截取字符串
#             if c != s2[i]:
#                 return s1[:i]
#         return s1
#
#
# if __name__ == '__main__':
#     s = Solution()
#     print(s.longestCommonPrefix(["flower", "flow", "flight"]))
#     print('123', s.longestCommonPrefix(["dog", "racecar", "car"]))
#
# def commonadd1(strs):
#     if not strs:
#         return ""
#     s1=min(strs)
#     s2=max(strs)
#     for i,j in enumerate(s1):
#         if j!=s2[i]:
#             if len(s1)>i+1:
#                 return s1[:i+1]
#             else:
#                 return s1[:i]
#     # return s1
#     for item in enumerate(strs):
#         lens=len(s1)-1
#         print(s1+item[lens])
#         return s1+item[lens]
# if __name__ == '__main__':
#     print(commonadd1(["flower", "flow", "flight"]))
#     print(commonadd1(["dog", "racecar", "car"]))


#
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         max_len = 0
#         if s is None or len(s) == 0:
#             return max_len
#         str_dict = {}
#         one_max = 0
#         start = 0
#         for i in range(len(s)):
#             if s[i] in str_dict and str_dict[s[i]] >= start:
#                 start = str_dict[s[i]] + 1
#             one_max = i - start + 1
#             str_dict[s[i]] = i
#             max_len = max(max_len, one_max)
#         return max_len
#
#
# if __name__ == '__main__':
#     sol = Solution()
#     print(sol.lengthOfLongestSubstring("bbbbb"))
#     print(sol.lengthOfLongestSubstring("eeydgwdykpv"))
#     print(sol.lengthOfLongestSubstring("pwwkew"))
#     print(sol.lengthOfLongestSubstring("abcabcbb"))


def substring(strs):
    liststr=strs.split(" ")
    result=[]
    count=0
    list0=[","]
    for item in range(len(liststr)):
        while item<len(liststr):
            if liststr[item] in result:
                if liststr[item] not in list0:
                    item+=1
            if liststr[item][-1]=="," or liststr[item][-1]=="!":
                    item+=1
            else:
                result.append(liststr[item])
                item+=1
                count+=1
    print("The number of words in this passage is:%d"%count)
    result=" ".join(result)
    return result


# one_str_list = ['120135435', 'abdfkjkgdok', '120135435','123456780423349']
one_str_list = "welcome to my house, my house is really big!"
b=substring(one_str_list)
print(b)

