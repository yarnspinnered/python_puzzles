#  Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
#
#     You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
#     Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

import heapq


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = []
        d = {}

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for key,v in d.items():
            h.append((-v, key))

        heapq.heapify(h)

        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])

        return res

s = Solution()
r = s.topKFrequent([1,2,3,3,2], 2)
print(r)