class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x

        if n > 0:
            if n % 2 == 0:
                return self.myPow(x*x, n//2)
            else:
                return x * self.myPow(x*x, n//2)
        else:
            n = -n
            if n % 2 == 0:
                return 1/self.myPow(x*x, n//2)
            else:
                return 1/x * 1/self.myPow(x*x, n//2)



s = Solution()
print(s.myPow(2.00000,-2147483648))