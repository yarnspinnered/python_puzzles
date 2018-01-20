#  Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
#     Only one letter can be changed at a time.
#     Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
#
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        all_chars = "abcdefghijklmnopqrstuvwxyz"
        visited = set()
        curr_frontier = set([beginWord])
        wordList = set(wordList)
        cnt = 1
        res = {}

        while curr_frontier:
            new_frontier = set()
            for w in curr_frontier:
                visited.add(w)
                for i in range(len(w)):
                    for c in all_chars:

                        candidate_nbr = w[:i] + c + w[i + 1:]
                        if candidate_nbr in wordList and candidate_nbr not in visited:
                            new_frontier.add(candidate_nbr)
            if endWord in new_frontier: return cnt + 1
            cnt += 1
            res[cnt] = curr_frontier
            curr_frontier = new_frontier

        return 0


s = Solution()
r = s.ladderLength("hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"])
print(r)
