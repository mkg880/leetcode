from collections import deque
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        vis = set()
        m, n = len(grid), len(grid[0])
        edgex = {0, m-1}
        edgey = {0, n-1}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in vis:
                    closed = i in edgex or j in edgey
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        if not 0 <= x < m or not 0 <= y < n or (x, y) in vis or grid[x][y] == 1:
                            continue
                        vis.add((x, y))
                        closed = closed or x in edgex or y in edgey
                        for dx, dy in directions:
                            q.append((x+dx, y+dy))
                    if not closed:
                        res += 1
        return res