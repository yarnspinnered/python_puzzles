import bisect
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        def bin_search_first_pos(matrix, target):
            l = 0
            r = len(matrix) - 1
            cand = 0
            while l <= r:
                m = (l + r)//2
                if matrix[m][0] < target:
                    cand = m
                    l = m + 1
                elif matrix[m][0] > target:
                    r = m - 1
                else:
                    return m
            return cand

        row = bin_search_first_pos(matrix, target)
        col = min(len(matrix[row]) - 1, bisect.bisect_left(matrix[row], target))
        return matrix[row][col] == target

s = Solution()
print(s.searchMatrix(
    [[1], [3]],
    3))