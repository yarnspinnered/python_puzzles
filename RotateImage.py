class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def layer_rotate(matrix, start_i, start_j, end_i, end_j):
            temp = matrix[start_i][start_j : end_j + 1]
            for i in range(start_i + 1, end_i + 1):
                temp.append(matrix[i][end_j])
            for i in range(start_i, end_i + 1):
                matrix[i][end_j] = temp.pop(0)

            for j in range(end_j - 1, start_j - 1, -1):
                temp.append(matrix[end_i][j])
            for j in range(end_j - 1, start_j -1, -1):
                matrix[end_i][j] = temp.pop(0)

            for i in range(end_i - 1, start_i -1, -1):
                temp.append(matrix[i][start_j])
            for i in range(end_i - 1, start_i -1, -1):
                matrix[i][start_j] = temp.pop(0)

            for j in range(start_j + 1, end_j + 1, 1):
                matrix[start_i][j] = temp.pop(0)
            return

        layer_count = len(matrix) // 2
        for layer in range(layer_count):
            layer_rotate(matrix, start_i= layer, start_j = layer, end_i = len(matrix) - 1 - layer, end_j = len(matrix) - 1 - layer)
        return

s = Solution()
l=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s.rotate(l)
print(l)