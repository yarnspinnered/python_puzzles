import math
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def permutation_helper(candidates, k):
            if len(candidates) == 1:
                return str(candidates[0])
            fact_val = math.factorial(len(candidates) - 1)
            index_to_remove = k // fact_val
            if k % fact_val == 0:
                index_to_remove -= 1
            x = candidates.pop(index_to_remove)

            next_k = k % fact_val
            if next_k == 0: next_k = fact_val

            return  str(x) + permutation_helper(candidates, k % fact_val)


        candidates = [i for i in range(1, n+1)]
        res_str = permutation_helper(candidates, k)

        return res_str


s = Solution()
print(s.getPermutation(3, 6))

