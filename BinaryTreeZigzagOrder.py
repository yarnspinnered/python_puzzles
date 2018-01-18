# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        curr_stk = [(0, root)]
        next_stk = []
        while curr_stk:
            lvl, curr = curr_stk.pop()
            if curr:
                if len(res) - 1 >= lvl:
                    res[lvl].append(curr.val)
                else:
                    res.append([curr.val])
                if lvl % 2 == 1:
                    next_stk.append((lvl + 1, curr.right))
                    next_stk.append((lvl + 1, curr.left))
                else:
                    next_stk.append((lvl + 1, curr.left))
                    next_stk.append((lvl + 1, curr.right))
            if not curr_stk:
                curr_stk = next_stk
                next_stk = []
        return res

