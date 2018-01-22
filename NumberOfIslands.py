# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
# is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        length = len(grid[0])
        height = len(grid)
        cnt = 0
        visited = [[False for x in range(length)] for x in range(height)]
        def explore(pos):
            curr_frontier = set([pos])
            while curr_frontier:
                next_frontier = set()
                for pos in curr_frontier:
                    i = pos[0]
                    j = pos[1]
                    visited[i][j] = True
                    if i > 0 and grid[i-1][j] == "1" and not visited[i-1][j]: next_frontier.add((i - 1, j))
                    if i < height - 1 and grid[i+1][j] == "1" and not visited[i+1][j]: next_frontier.add((i + 1, j))
                    if j > 0 and grid[i][j-1] == "1" and not visited[i][j-1]: next_frontier.add((i, j - 1))
                    if j < length - 1 and grid[i][j+1] == "1" and not visited[i][j+1]: next_frontier.add((i, j + 1))
                curr_frontier = next_frontier



        for i in range(height):
            for j in range(length):
                if grid[i][j] == "1" and not visited[i][j]:
                    explore((i, j))
                    cnt += 1

        return cnt

s = Solution()
res = s.numIslands([["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]])
print(res)