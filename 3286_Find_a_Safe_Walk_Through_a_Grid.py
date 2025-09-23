from collections import deque
from typing import List
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque([(0, 0, health - grid[0][0])])
        visited = {}
        while q:
            i, j, h = q.popleft()
            if h == 0 or ((i, j) in visited and visited[(i, j)] >= h):
                continue
            if (i, j) == (m-1, n-1):
                return True
            visited[(i, j)] = h
            for a, b in directions:
                x, y = a + i, b + j
                if x >= 0 and x < m and y >= 0 and y < n:
                    q.append((x, y, h - grid[x][y]))
        return False