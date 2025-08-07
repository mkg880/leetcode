class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if isinstance(matrix[i][0], tuple):
                        _, col = matrix[i][0]
                    else:
                        col = False
                    matrix[i][0] = (True, col)
                    if isinstance(matrix[0][j], tuple):
                        row, _ = matrix[0][j]
                    else:
                        row = False
                    matrix[0][j] = (row, True)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if isinstance(matrix[i][0], tuple):
                    row, _ = matrix[i][0]
                    if row:
                        matrix[i][j] = 0
                if isinstance(matrix[0][j], tuple):
                    _, col = matrix[0][j]
                    if col:
                        matrix[i][j] = 0