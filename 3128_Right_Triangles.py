class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += (row[i] - 1) * (col[j] - 1)
        return res