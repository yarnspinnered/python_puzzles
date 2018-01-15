class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        direction = 1
        ptr = 0
        list_of_strs = ["" for x in range(numRows)]

        if numRows == 1:
            return s

        for c in s:
            list_of_strs[ptr] += c
            ptr = ptr + direction
            if ptr == numRows:
                ptr = numRows - 2
                direction = -1
            elif ptr == -1:
                ptr = 1
                direction = 1

        result = ""
        for substr in list_of_strs:
            result = result + substr

        return result

s = Solution()
print(s.convert("PAYPALISHIRING", 3))