# So many edge cases.
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if int(s) == 0 or s[0] == "0":
            return 0

        res = [0] * (len(s) + 1)
        if s[-1] == "0":
            res[len(s) - 1] = 0
        else:
            res[len(s) - 1] = 1

        res[len(s)] = 1
        for i in range(len(s) - 2, -1, -1):
            two_digit = int(s[i:i +2])
            if (two_digit > 26 and s[i+1] == "0") or two_digit == 0:
                return 0
            if two_digit == 10 or two_digit == 20:
                res[i] = res[i + 2]
            elif 11 <= two_digit <= 26:
                res[i] = res[i + 1] + res[i + 2]
            else:
                res[i] = res[i+1]
        return res[0]

s = Solution()
print(s.numDecodings("7206"))