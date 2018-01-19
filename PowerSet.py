class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        next = self.subsets(nums[1:])
        res = []
        res.extend(next)
        for n in next:
            res.append([nums[0]] + n)
        return res

s = Solution()
print(s.subsets([1,2,3]))