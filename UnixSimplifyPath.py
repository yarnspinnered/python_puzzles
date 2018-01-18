class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stk = []
        cancel_flag = False
        res = ""
        split_path = path.split("/")
        for i in range(len(split_path)-1, -1, -1):
            if split_path[i] == "/":
                continue
            elif split_path[i] == "":
                continue
            elif split_path[i] == ".":
                stk.append(".")
            elif split_path[i] == "..":
                stk.append("..")
            else:
                while len(stk) > 0:
                    op = stk.pop()
                    if op == ".":
                        continue
                    elif op == "..":
                        cancel_flag = True
                        break
                if not cancel_flag:
                    res = "/" + split_path[i] + res
                cancel_flag = False

        if res == "": res = "/"

        return res

s = Solution()
print(s.simplifyPath("/a/./b/../../c/"))