class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return []


        def checkPalindromic(word):
            for i in range(len(word)//2):
                if word[i] != word[len(word) - 1 - i]:
                    return False
            return True

        res = []

        if checkPalindromic(s):
            res.append([s])

        for i in range(1, len(s)):
            if checkPalindromic(s[:i]):
                next = self.partition(s[i:])
                for part in next:
                    new = part[:]
                    new.insert(0,s[:i])
                    res.append(new)

        return res

s = Solution()
print(s.partition("aabaa"))