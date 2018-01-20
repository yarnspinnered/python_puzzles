#  Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        segmentable = [False for x in range(len(s) + 1)]
        segmentable[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if segmentable[j] and s[j: i] in wordDict:
                    segmentable[i] = True
                    break

        return segmentable[-1]

s = Solution()
r = s.wordBreak("leetcode", ["leet", "code"])
print(r)
