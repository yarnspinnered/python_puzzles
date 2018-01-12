class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        sol_array =[[0]*n for i in range(m)]
        sol_array[0] = [1 for i in range(n)]

        for i in range(1,m):
            for j in range(n):
                row = i % m
                col = j % n
                if col == 0:
                    sol_array[row][col] = sol_array[row - 1][col]
                else:
                    sol_array[row][col] = sol_array[row - 1][col] + sol_array[row][col - 1]

        return sol_array[m-1][n-1]


s = Solution()
print(s.uniquePaths(2,3))