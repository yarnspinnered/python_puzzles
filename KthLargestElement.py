import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heapq.heapify(nums)
        res = heapq.nlargest(k, nums)

        return res[-1]

s = Solution()
s.findKthLargest([5,4,3,2,1,6], 3)