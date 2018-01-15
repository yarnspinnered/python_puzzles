# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        prev = None
        first = head
        second = head.next
        after = head.next.next

        while first and second:
            if prev:
                prev.next = second
            else:
                head = second
            second.next = first
            first.next = after

            first = after
            if first:
                second = first.next
                if second:
                    after = second.next
                else:
                    return head
            else:
                return head
