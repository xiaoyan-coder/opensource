# @Time : 2020/8/7 20:47 
# @Author : 小小
# @File : sametree.py 
# @Software: PyCharm
# Definition for a binary tree node.
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
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



