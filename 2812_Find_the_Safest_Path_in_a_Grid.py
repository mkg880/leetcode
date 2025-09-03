from collections import deque
from math import ceil
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dist = {}
        n = len(grid)
        q = deque([(i, j, 0) for j in range(n) for i in range(n) if grid[i][j]])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            x, y, d = q.popleft()
            if not 0 <= x < n or not 0 <= y < n or (x, y) in dist:
                continue
            dist[(x, y)] = d
            for dx, dy in directions:
                q.append((x+dx, y+dy, d+1))
        def possible(min_dist):
            q = deque([(0, 0)])
            vis = set()
            while q:
                x, y = q.popleft()
                if not 0 <= x < n or not 0 <= y < n or (x, y) in vis or dist[(x, y)] < min_dist:
                    continue
                vis.add((x, y))
                if (x, y) == (n-1, n-1):
                    return True
                for dx, dy in directions:
                    q.append((x+dx, y+dy))
            return False
        lo, hi = 0, max(dist.values())
        while lo < hi:
            mid = ceil((lo + hi) / 2)
            if possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo