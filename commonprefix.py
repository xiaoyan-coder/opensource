# @Time : 2020/8/7 20:47 
# @Author : 小小
# @File : sametree.py 
# @Software: PyCharm

# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""
# 解题思路：1.如果这个list字符串是空的，返回空，2.先找出最大跟最小的字符串，然后遍历当找到两个子串不一致的地方就返回
# 不一致前的子串，就是最长的公告呢子串公共前缀3.如果循环结束了，还是没有找到两个子串不一致的地方，那么返回最小子串
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0

res1=Solution().longestCommonPrefix( ["fac","facecar","fa"])
print(res1)

