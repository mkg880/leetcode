class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) in visited or grid[i][j] == 0:
                    continue
                stack = [(i, j)]
                amt = 0
                while stack:
                    a, b = stack.pop()
                    if (a, b) in visited or grid[a][b] == 0:
                        continue
                    visited.add((a, b))
                    amt += grid[a][b]
                    for x, y in directions:
                        c, d = x + a, y + b
                        if 0 <= c < m and 0 <= d < n:
                            stack.append((c, d))
                res = max(res, amt)
        return res