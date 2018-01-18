# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        first = head
        second = head

        length = 0
        ctr = head
        while ctr != None:
            ctr = ctr.next
            length += 1

        if length == 0:
            return head
        else:
            k = k % length

        for i in range(k):
            second = second.next

        while second.next != None:
            first = first.next
            second = second.next

        second.next = head
        head = first.next
        first.next = None

        return head