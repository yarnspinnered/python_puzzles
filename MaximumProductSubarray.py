#  Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = nums[0]
        biggest = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            old_smallest = smallest
            smallest = min(min(nums[i] * smallest, nums[i] * biggest), nums[i])
            biggest = max(max(nums[i] * old_smallest, nums[i] * biggest), nums[i])
            res = max(res, biggest)
        return res


s = Solution()
r = s.maxProduct([1,2,3,0,24,5,2])
print(r)
