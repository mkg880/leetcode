class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i, j) in vis:
                    continue
                stack = [(i, j, None, None)]
                while stack:
                    x, y, prevx, prevy = stack.pop()
                    if (x, y) in vis:
                        return True
                    vis.add((x, y))
                    for dx, dy in directions:
                        newx, newy = x+dx, y+dy
                        if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == grid[x][y] and (newx, newy) != (prevx, prevy):
                            stack.append((newx, newy, x, y))
        return False