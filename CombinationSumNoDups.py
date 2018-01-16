import itertools
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = [[] for x in range(target + 1)]

        for candidate in candidates:
            if candidate > target:
                continue

            new_lst = [[] for x in range(candidate, target + 1)]
            new_lst[0].append([candidate])

            for i in range(candidate, target + 1):
                prev_res_lst = res[i - candidate]
                if prev_res_lst:
                    for prev_lst in prev_res_lst:
                        new_lst[i - candidate].append(prev_lst + [candidate])

            for i, new_items in enumerate(new_lst):
                res[i + candidate].extend(new_lst[i])

        final_result = set()
        for ans in res[target]:
            ans.sort()
            final_result.add((tuple(ans)))

        return [list(x) for x in final_result]

s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))