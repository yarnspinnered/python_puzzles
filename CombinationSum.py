class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = [[] for x in range(target + 1)]

        for candidate in candidates:
            if candidate > target:
                continue
            ret[candidate].append([candidate])
            for i in range(candidate, target + 1):
                for prev_lst in ret[i-candidate]:
                    if prev_lst:
                        ret[i].append(prev_lst + [candidate])
        return ret[target]

s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))


