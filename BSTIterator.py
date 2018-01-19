# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

        if self.stack:
            self.root = self.stack.pop()
            self.fill_stack()
        else:
            self.root = None

    def fill_stack(self):
        curr = self.root
        if curr and curr.right:
            self.stack.append(curr.right)
            curr = curr.right.left
            while curr:
                self.stack.append(curr)
                curr = curr.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.root != None

    def next(self):
        """
        :rtype: int
        """
        res = self.root.val
        if self.stack:
            self.root = self.stack.pop()
            if self.root.right:
                self.fill_stack()
        else:
            self.root = None
        return res

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())