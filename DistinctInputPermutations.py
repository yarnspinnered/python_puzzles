class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [[nums[0]]]

        prev = self.permute(nums[:-1])
        curr_num = nums[-1]
        res = []

        for prev_lst in prev:
            for i in range(len(prev_lst) + 1):
                temp_lst = prev_lst[:]
                temp_lst.insert(i, curr_num)
                res.append(temp_lst)

        return res


s = Solution()
print(s.permute([1,2,3]))