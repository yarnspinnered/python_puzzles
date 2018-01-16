import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        ret = []

        if l == r or l >= len(nums):
            return [-1, -1]
        else:
            return [l, r - 1]

s = Solution()
nums=[5, 7, 7, 8, 8, 10]
print(s.searchRange(nums, 10))
