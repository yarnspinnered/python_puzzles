# Given a binary tree, flatten it to a linked list in-place.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def flatten_helper(root):
            if not root:
                return None,None

            left_start, left_end = flatten_helper(root.left)
            right_start, right_end = flatten_helper(root.right)

            root.left = None

            if left_end and right_start:
                root.right = left_start
                left_end.right = right_start
                return root, right_end
            elif left_end and not right_start:
                root.right = left_start
                return root, left_end
            elif not left_end and right_start:
                root.right = right_start
                return root, right_end
            else:
                return root, root


        flatten_helper(root)

s1 = TreeNode(1)
s2 = TreeNode(2)
s1.left = s2
s = Solution()
s.flatten(s1)
print(s1.right)
