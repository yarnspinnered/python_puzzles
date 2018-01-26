class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(n1, n2):
            if n1 == n2:
                return True
            elif n1 + n2 > n2 + n1:
                return True
            else:
                return False


        def helper(arr):
            if len(arr) == 1:
                return arr
            m = len(arr) // 2
            left = helper(arr[:m])
            right = helper(arr[m:])
            res = []

            while left and right:
                if compare(str(left[0]), str(right[0])):
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))

            res.extend(left)
            res.extend(right)

            return res

        res_arr = helper(nums)
        res_str = "".join(str(x) for x in res_arr)
        res_str = res_str[:-1].lstrip("0") + res_str[-1]
        return res_str

s = Solution()
r = s.largestNumber( [20,1])
print(r)


