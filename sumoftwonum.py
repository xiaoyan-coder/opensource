'''
两数之和
给定一个整数数组nums和一个目标值target，请你在该数组中找出和为
目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
给定
nums = [2, 7, 11, 15], target = 9
因为
nums[0] + nums[1] = 2 + 7 = 9
所以返回[0, 1]
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 设置两层循环，第一层循环，从第一个数字到倒数第二个数字。第一层循环中的每一个数字与相邻的数字相加一次
        for i in range(0,len(nums)-1):
            # 第二层循环，从第二个数字(即i+1),一直比对到最后一个数字
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    # 如果有相等就返回下标
                    return [i,j]
a=Solution().twoSum([2, 7, 11, 15],9)
print(a)