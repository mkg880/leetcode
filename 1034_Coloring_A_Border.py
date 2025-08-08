class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = [(row, col)]
        vis = set()
        init_color = grid[row][col]
        while stack:
            x, y = stack.pop()
            if (x, y) in vis:
                continue
            vis.add((x, y))
            for dx, dy in dirs:
                new_x, new_y = dx+x, dy+y
                if (new_x, new_y) in vis:
                    continue
                if not 0 <= new_x < m or not 0 <= new_y < n or grid[new_x][new_y] != init_color:
                    grid[x][y] = color
                else:
                    stack.append((new_x, new_y))
        return grid