class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_pos = len(nums) - 1

        if last_pos <= 1:
            return True
        total_jump = nums[0] + nums[nums[0]]
        curr_pos = 0

        while total_jump < last_pos and nums[curr_pos] != 0:
            curr_jump_range = nums[curr_pos]

            if curr_jump_range + curr_pos >= last_pos:
                return True

            for i in range(curr_pos + 1, curr_jump_range + curr_pos):
                if nums[nums[i]] + nums[i] + i >= total_jump:
                    total_jump = nums[nums[i]] + nums[i] + i
                    curr_pos = nums[i] + i



        return curr_pos >= (last_pos - 1)
s = Solution()
print(s.canJump([2,3,1,1,4]))

print(s.canJump([3,2,1,0,4]))