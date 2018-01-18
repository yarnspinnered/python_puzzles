class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        res = [[0] * len(obstacleGrid[0]) for x in range(len(obstacleGrid))]
        if obstacleGrid[0][0] == 0:
            res[0][0] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    if i > 0 and j > 0:
                        res[i][j] = res[i-1][j] + res[i][j-1]
                    elif i > 0:
                        res[i][j] = res[i-1][j]
                    elif j > 0:
                        res[i][j] = res[i][j-1]

        return res[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]