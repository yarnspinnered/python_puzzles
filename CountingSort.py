class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ctrs = [0, 0, 0]

        for x in nums:
            ctrs[x] += 1

        current_ctr = 0

        for i in range(len(nums)):
            if ctrs[current_ctr] > 0:
                nums[i] = current_ctr
            else:
                while ctrs[current_ctr] <= 0:
                    current_ctr += 1
                nums[i] = current_ctr
            ctrs[current_ctr] -= 1

s = Solution()
l = [2]
s.sortColors(l)
print(l)