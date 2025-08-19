from collections import deque
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        vis = set()
        m, n = len(land), len(land[0])
        res = []
        directions = [(0, 1), (1, 0)]
        for i in range(m):
            for j in range(n):
                if not land[i][j] or (i, j) in vis:
                    continue
                q = deque([(i, j)])
                k, l = i, j
                while q:
                    x, y = q.popleft()
                    if not 0 <= x < m or not 0 <= y < n or (x, y) in vis or not land[x][y]:
                        continue
                    vis.add((x, y))
                    if x > k or (x == k and y > l):
                        k, l = x, y
                    for dx, dy in directions:
                        q.append((x+dx, y+dy))
                res.append([i, j, k, l])
        return res