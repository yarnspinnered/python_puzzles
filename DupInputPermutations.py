class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]

        prev = self.permuteUnique(nums[:-1])
        res = set()
        curr_num = nums[-1]

        for prev_perm in prev:
            for i in range(len(prev_perm) + 1):
                new_lst = prev_perm[:]
                new_lst.insert(i, curr_num)
                res.add(tuple(new_lst))

        final_res = []
        for tup in res:
            final_res.append(list(tup))
        return final_res

s = Solution()
print(s.permuteUnique([1,2,2]))