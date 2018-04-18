class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == "#":
            return True

        arr = preorder.split(",")
        stk = [[arr.pop(0),0]]
        for c in arr:
            if not stk or len(stk)==1 and stk[-1][0] == "#":
                return False
            stk_top = stk[-1]
            if stk_top[1] == 0:
                stk_top[1] += 1
            elif stk_top[1] == 1:
                stk.pop()
            if c != "#":
                stk.append([c, 0])


        return not stk

s = Solution()
print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
print(s.isValidSerialization("9,#,#,1"))
print(s.isValidSerialization("1,#"))