class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        count = {}
        if len(s) <= 1:
            return len(s)

        best = 1
        max_j = 0
        i = 0
        for j in range(len(s)):
            if s[j] in count:
                count[s[j]] += 1
            else:
                count[s[j]] = 1

            if count[s[j]] > max_j:
                max_j = count[s[j]]

            if (j - i + 1) - max_j <= k:
                best = max(best, j - i + 1)
            else:
                count[s[i]] -= 1
                i += 1


        return max(best, j - i + 1)



s = Solution()
s.characterReplacement("ABABC",2)




