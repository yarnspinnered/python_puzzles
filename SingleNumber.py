#  Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in nums:
            if x in d.keys():
                d[x] += 1
            else:
                d[x] = 1

        res = min(d, key=d.get)
        return res

s = Solution()
print(s.singleNumber([1,1,1,3,5,5]))