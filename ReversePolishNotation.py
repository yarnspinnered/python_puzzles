class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])

        s = []
        operators = frozenset(["*", "+", "-", "/"])

        for i in range(len(tokens) - 1, -1, -1):
            s.append(tokens[i])
            if s[-1] in operators:
                continue
            else:
                if s[-2] in operators:
                    continue
                else:
                    while len(s) >= 3 and s[-1] not in operators and s[-2] not in operators:
                        num = int(s.pop())
                        other_num = int(s.pop())
                        op = s.pop()
                        if op == "*":
                            res = num * other_num
                        elif op == "/":
                            res = num / other_num
                        elif op == "-":
                            res = num - other_num
                        elif op == "+":
                            res = num + other_num
                        s.append(res)
        return int(s[0])

s = Solution()
print(s.evalRPN(  ["2", "1", "+", "3", "*"]))