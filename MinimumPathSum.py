class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        result = [[0] * len(grid[0]) for x in range(len(grid))]

        result[0][0] = grid[0][0]
        for j in range(1, len(grid[0]) ):
            result[0][j] += result[0][j-1] + grid[0][j]
        for i in range(1, len(grid)):
            result[i][0] += result[i-1][0] + grid[i][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                result[i][j] = min(result[i - 1][j], result[i][j-1]) + grid[i][j]

        return result[len(grid) - 1][len(grid[0]) - 1]

s = Solution()
print(s.minPathSum([[1,3,1],
 [1,5,1],
 [4,2,1]]))