# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        q = [(0,root)]
        res = [[]]

        while q:
            lvl, curr = q.pop(0)
            if curr != None:
                if len(res) - 1 < lvl:
                    res.append([curr.val])
                else:
                    res[lvl].append(curr.val)
                q.append((lvl + 1, curr.left))
                q.append((lvl + 1, curr.right))

        return res
