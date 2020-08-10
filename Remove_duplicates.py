# @Time : 2020/8/7 20:47 
# @Author : 小小
# @File : sametree.py 
# @Software: PyCharm
'''
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。
'''
# 解题思路：定义两个指针，分别先指向第一个元素跟第二个元素
# 循环中对比，如果第一个元素跟第二个元素相同，则删除第二个元素，如果两个元素不同，则两个指针分别下移，指向不同的元素
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L,R=0,1
        while R<len(nums):
            # 如果相邻的两个元素相同，则删除后一个元素
            if nums[L]==nums[R]:
                nums.pop(R)
            # 如果相邻的两个元素不同，两个指针各自加1，再比对另外两个相邻的元素
            else:
                L+=1
                R+=1
        return len(nums)
res1=Solution().removeDuplicates([1,1,2])
print(res1)

