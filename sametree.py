# @Time : 2020/8/7 20:47 
# @Author : 小小
# @File : sametree.py 
# @Software: PyCharm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==q==None:
            return True
        elif p!=None and q==None:
            return False
        elif q!=None and p==None:
            return False
        elif p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)



