class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        if n == 1:
            return ["()"]
        s = Solution()

        previous = s.generateParenthesis(n-1)
        res = set()

        for paren_str in previous:
            for i in range(len(paren_str)):
                res.add(paren_str[:i] + "()" + paren_str[i:])
            res.add(paren_str + "()")


        return list(res)
s = Solution()
print(s.generateParenthesis(3))