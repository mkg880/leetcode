class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = set()
        i, j = 0, 0
        d = 0
        cnt = 1
        while cnt <= n * n:
            res[i][j] = cnt
            vis.add((i, j))
            di, dj = dirs[d]
            x, y = i+di, j+dj
            if not 0 <= x < n or not 0 <= y < n or (x, y) in vis:
                d += 1
                d %= 4
                di, dj = dirs[d]
                x, y = i+di, j+dj
            i, j = x, y
            cnt += 1
        return res