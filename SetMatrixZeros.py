class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = [1] * len(matrix)
        col = [1] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0

        for r in range(len(row)):
            if row[r] == 0:
                matrix[r] = [0] * len(matrix[0])

        for c in range(len(col)):
            if col[c] == 0:
                for i in range(len(matrix)):
                    matrix[i][c] = 0

        return

