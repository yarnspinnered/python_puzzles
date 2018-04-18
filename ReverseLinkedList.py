"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""


def Reverse(head):
    curr = head
    one_before = None

    while curr:
        next = curr.next
        curr.next = curr.prev
        curr.prev = next
        one_before = curr
        curr = next

    if one_before:
        return one_before
    else:
        return curr












