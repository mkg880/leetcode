from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        edge_x = [0, m-1]
        edge_y = [0, n-1]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = set()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i, j) in vis:
                    continue
                q = deque([(i, j)])
                cnt = 0
                enclave = True
                while q:
                    x, y = q.popleft()
                    if not 0 <= x < m or not 0 <= y < n or grid[x][y] == 0 or (x, y) in vis:
                        continue
                    vis.add((x, y))
                    cnt += 1
                    if x in edge_x or y in edge_y:
                        enclave = False
                    for dx, dy in directions:
                        q.append((x+dx, y+dy))
                if enclave:
                    res += cnt
        return res