# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        def merge(u,v):

            if u.val <= v.val:
                curr = u
                u = u.next
            else:
                curr = v
                v = v.next

            start = curr
            while u and v:
                if u.val <= v.val:
                    curr.next = u
                    curr = curr.next
                    u = u.next
                else:
                    curr.next = v
                    curr = curr.next
                    v = v.next
            if u:
                curr.next = u
            else:
                curr.next = v

            return start

        prev = None
        first = head
        second = head.next

        while second and second.next:
            prev = first
            first = first.next
            second = second.next.next

        if prev:
            prev.next = None
            second_start = first
        else:
            first.next = None
            second_start = second

        part1 = self.sortList(head)
        part2 = self.sortList(second_start)
        return merge(part1, part2)

s = Solution()
a = ListNode(3)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next = c
res = s.sortList(a)

while res:
    print(res.val)
    res = res.next