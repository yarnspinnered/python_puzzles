# Definition for singly-linked list.



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def oneListToInt(l):
            res = 0
            multiplier = 1
            while l is not None:
                res += l.val * multiplier
                multiplier = multiplier * 10
                l = l.next
            return res

        res = 0
        carry_over = 0
        multiplier = 1


        while l1 is not None and l2 is not None:
            # print(l1.val * l2.val + carry_over)
            res += multiplier * ((l1.val + l2.val + carry_over) % 10)
            carry_over = (l1.val + l2.val + carry_over) // 10
            multiplier = multiplier * 10
            # print("RES: " + str(res))
            l1 = l1.next
            l2 = l2.next

        l1_extra = oneListToInt(l1)
        l2_extra = oneListToInt(l2)
        res = (l1_extra + l2_extra + carry_over) * multiplier + res
        print("RES: " + str(res))

        head = ListNode(res % 10)
        res_ll = head
        res = res // 10
        print("INIT RES " + str(res))

        while res > 0:
            new_node = ListNode(res%10)
            res_ll.next = new_node
            res_ll = new_node
            res = res // 10
            print("ITER RES " + str(res))


        return head

l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)
l2_1.next = l2_2
# l2_2.next = l2_3

sol = Solution()
sol.addTwoNumbers(l1_1,l2_1)
