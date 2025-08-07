from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                q = deque([(i, j, 0)])
                vis = set()
                found = False
                while q:
                    x, y, d = q.popleft()
                    if not 0 <= x < m or not 0 <= y < n or (x, y) in vis or grid[x][y] == 0:
                        continue
                    vis.add((x, y))
                    if grid[x][y] == 2:
                        found = True
                        res = max(res, d)
                        break
                    for dx, dy in directions:
                        q.append((x+dx, y+dy, d+1))
                if not found:
                    return -1
        return res