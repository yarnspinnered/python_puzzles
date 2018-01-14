class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        answers = [0] * (n + 1)
        answers[0] = 1
        answers[1] = 1

        for i in range(2, n-1):
            ans_i = 0
            for j in range(0,n):
                ans_i += answers[j]
            answers[i] = ans_i

        return answers[n]

s = Solution()
print(s.numTrees(3))
