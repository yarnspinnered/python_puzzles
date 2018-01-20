class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def combine_helper(start, k, cache):
            if n - start < 0:
                return []
            if (start, k) in cache.keys():
                return cache[(start, k)]
            res = []
            for combination in combine_helper(start + 1, k - 1, cache):
                res.append([start] + combination[:])
            for combination in combine_helper(start + 1, k, cache):
                res.append(combination[:])
            return res

        c = {}
        for i in range(1, n + 1):
            c[(i, 1)] = [[x] for x in range(i, n + 1)]

        res = combine_helper(1, k, c)

        return res

s = Solution()
print(s.combine(4,3))