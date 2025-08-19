from collections import deque
from typing import List
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(heights), len(heights[0])
        def possible(k):
            q = deque([(0, 0)])
            vis = set()
            while q:
                x, y = q.popleft()
                if (x, y) in vis:
                    continue
                if (x, y) == (m-1, n-1):
                    return True
                vis.add((x, y))
                for dx, dy in directions:
                    newx, newy = x+dx, y+dy
                    if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in vis and abs(heights[newx][newy] - heights[x][y]) <= k:
                        q.append((newx, newy))
            return False
        lo, hi = 0, 10 ** 6
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid+1
        return lo