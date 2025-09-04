from collections import deque
from typing import Counter
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        c = Counter()
        for start in range(n):
            dist = [float('inf')] * n
            q = deque([(start, 0)])
            while q:
                curr, d = q.popleft()
                if dist[curr] < d:
                    continue
                dist[curr] = d
                if curr > 0:
                    q.append((curr-1, d+1))
                if curr < n-1:
                    q.append((curr+1, d+1))
                if curr == x-1:
                    q.append((y-1, d+1))
                if curr == y-1:
                    q.append((x-1, d+1))
            c.update(dist)
        return [c.get(i+1, 0) for i in range(n)]