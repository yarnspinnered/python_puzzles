class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if tot < 0:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif tot > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return [list(x) for x in res]

s = Solution()
print(s.threeSum([-2,0,1,1,2]))