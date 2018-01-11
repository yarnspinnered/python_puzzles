class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        s = Solution()
        phone_dict = {"0":" ",
                      "2":"abc",
                      "3":"def",
                      "4":"ghi",
                      "5":"jkl",
                      "6":"mno",
                      "7":"pqrs",
                      "8":"tuv",
                      "9":"wxyz"}

        if len(digits) < 1:
            return []
        elif len(digits) == 1:
            return list(phone_dict[digits])
        else:
            res = []
            prev = s.letterCombinations(digits[:-1])
            for combo in prev:
                for corresponding_char in phone_dict[digits[-1]]:
                    res.append(combo + corresponding_char)
            return res

s = Solution()
print(s.letterCombinations("234"))