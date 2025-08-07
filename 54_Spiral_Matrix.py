class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = set()
        res = []
        i, j = 0, 0
        d = 0
        while len(vis) < m * n:
            res.append(matrix[i][j])
            vis.add((i, j))
            di, dj = dirs[d]
            x, y = i+di, j+dj
            if not 0 <= x < m or not 0 <= y < n or (x, y) in vis:
                d += 1
                d %= 4
                di, dj = dirs[d]
                x, y = i+di, j+dj
            i, j = x, y
        return res