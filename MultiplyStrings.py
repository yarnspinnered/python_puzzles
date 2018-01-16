class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            shorter = len(num1) - 1
            shorter_word = num1

            longer = len(num2) - 1
            longer_word = num2
        else:
            shorter = len(num2) - 1
            shorter_word = num2

            longer = len(num1) - 1
            longer_word = num1

        res = 0
        offset = 1

        while shorter >= 0:
            temp_offset = offset
            for l in range(longer, -1, -1):
                res += temp_offset * int(shorter_word[shorter]) * int(longer_word[l])
                temp_offset *= 10
            offset *= 10
            shorter -= 1

        return str(res)

s = Solution()
print(s.multiply("98","9"))
