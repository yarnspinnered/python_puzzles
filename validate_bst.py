# Definition for a binary tree node.
import math
import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root, lo=-2**31-1,hi=2**31+1):
        """
        :type root: TreeNode
        :rtype: bool
        """

        s = Solution()
        flag = True
        # print(str(root.val) + " low: " + str(lo) + " high: " + str(hi))
        if root is None:
            return True


        if root.val > hi or root.val < lo:
            return False
        if root.left is None and root.right is None:
            return True

        if root.left is not None:
            flag = flag and root.val > root.left.val and s.isValidBST(root.left, lo =lo, hi = min(root.val - 1,hi))

        if root.right is not None:

            flag = flag and root.val < root.right.val and s.isValidBST(root.right, lo = max(root.val + 1,lo), hi= hi)
        return flag

x1 = TreeNode(10)
x2 = TreeNode(5)
x3 = TreeNode(15)
x4 = TreeNode(6)
x5 = TreeNode(20)

x1.left = x2
x1.right = x3
x3.left = x4
x3.right = x5

s = Solution()
print(s.isValidBST(x1))