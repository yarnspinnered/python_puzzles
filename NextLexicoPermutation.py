class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        def reverse_subarr(A, l, r):
            while l < r:
                temp = A[l]
                A[l] = A[r]
                A[r] = temp
                l += 1
                r -= 1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                j = i
                while j < len(nums) and nums[j] > nums[i-1]:
                    smallest = nums[j]
                    smallest_i = j
                    j += 1
                nums[smallest_i] = nums[i-1]
                nums[i-1] = smallest
                reverse_subarr(nums, i , len(nums) - 1)
                return

        reverse_subarr(nums, 0, len(nums) - 1)
        return

s = Solution()
l = [1,3,2]
s.nextPermutation(l)
print(l)