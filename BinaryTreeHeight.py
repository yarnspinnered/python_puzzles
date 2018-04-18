# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    if not root:
        return -1
    l_h = height(root.left)
    r_h = height(root.right)
    return max(l_h + 1, r_h + 1)