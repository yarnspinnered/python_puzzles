# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_val(self, lst, val):
        for i,x in enumerate(lst):
            if x == val: return i

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        in_order_pos = self.find_val(inorder, root_val)

        root.left = self.buildTree(preorder, inorder[:in_order_pos])
        root.right = self.buildTree(preorder, inorder[in_order_pos + 1:])

        return root

s = Solution()
r = s.buildTree([1,2],[1,2])

def in_order_walk(root):
    if root == None:
        return
    in_order_walk(root.left)
    print(root.val)
    in_order_walk(root.right)

in_order_walk(r)