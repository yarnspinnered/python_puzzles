# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
#     You may only use constant extra space.
#     You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def connect_helper(node, next):
            if not node:
                return
            node.next = next
            connect_helper(node.left, node.right)
            if next:
                connect_helper(node.right, next.left)
            else:
                connect_helper(node.right, None)

        connect_helper(root, None)

s = Solution()
s.connect(root)