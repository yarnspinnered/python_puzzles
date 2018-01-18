class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        max_cost = 2**32 - 1
        cost_triangle = [[max_cost] * len(lvl) for lvl in triangle]
        cost_triangle[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    cost_triangle[i][j] = cost_triangle[i-1][0] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    cost_triangle[i][j] = cost_triangle[i - 1][-1] + triangle[i][j]
                else:
                    cost_triangle[i][j] = min(cost_triangle[i - 1][j-1], cost_triangle[i-1][j]) + triangle[i][j]

        return min(cost_triangle[-1])

s = Solution()
print(s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))