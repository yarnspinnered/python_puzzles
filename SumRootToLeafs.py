import math
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sum_helper(node):
            if not node:
                return []
            temp = []
            res = []
            if node.left:
                temp.extend(sum_helper(node.left))
            if node.right:
                temp.extend(sum_helper(node.right))
            if temp:
                for t in temp:
                    res.append(str(node.val) + t)
            else:
                return [str(node.val)]
            return res

        all_paths = sum_helper(root)
        total_value = 0
        for p in all_paths:
            total_value += int(p)
        return total_value


