# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small_end = None
        small_start = None
        big_end = None
        big_start = None
        curr = head

        while curr:
            if curr.val < x:
                if small_end:
                    small_end.next = curr
                    small_end = curr
                else:
                    small_start = curr
                    small_end = curr
            else:
                if big_end:
                    big_end.next = curr
                    big_end = curr
                else:
                    big_start = curr
                    big_end = curr
            curr = curr.next

        if not small_end or not big_end:
            return head

        small_end.next = big_start
        big_end.next = None
        return small_start

