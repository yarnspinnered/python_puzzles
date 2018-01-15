# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        second = head

        for i in range(n):
            second = second.next

        while second is not None:
            prev = first
            first = first.next
            second = second.next

        if prev is None:
            head = first.next
        else:
            prev.next = first.next

        return head

