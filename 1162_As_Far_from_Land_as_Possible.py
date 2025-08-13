from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        land = []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    land.append((i, j, 0))
        q = deque(land)
        vis = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        while q:
            x, y, d = q.popleft()
            if not 0 <= x < n or not 0 <= y < n or (x, y) in vis:
                continue
            vis.add((x, y))
            res = max(res, d)
            for dx, dy in directions:
                q.append((x+dx, y+dy, d+1))
        return res if res > 0 else -1