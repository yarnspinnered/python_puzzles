import heapq
import math

class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        candidate_words = {}
        full_alphabet = "abcdefghijklmnopqrstuvwxyz"
        word_sets = []
        for word in words:
            word_sets.append((frozenset(word), len(word)))

        max_length = 0

        for word in words:
            word_set_form = frozenset(word)
            for other_word in word_sets:
                if word_set_form.isdisjoint(other_word[0]):
                    max_length = max(max_length, len(word) * other_word[1])


        return max_length

s = Solution()
print(s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))