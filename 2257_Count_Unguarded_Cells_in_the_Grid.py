from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i, j in walls:
            grid[i][j] = 2
        for i, j in guards:
            grid[i][j] = 1
            for k in range(4):
                end = {1, 2, -(k+1)}
                dx, dy = directions[k]
                x, y = i+dx, j+dy
                while 0 <= x < m and 0 <= y < n and grid[x][y] not in end:
                    grid[x][y] = -(k+1)
                    x, y = x+dx, y+dy
        return sum(1 if not grid[i][j] else 0 for i in range(m) for j in range(n))
