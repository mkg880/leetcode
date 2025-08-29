class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0]:
            return False
        n = len(grid)
        x, y = 0, 0
        total = n ** 2
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for i in range(1, total):
            found = False
            for dx, dy in directions:
                a, b = x+dx, y+dy
                if 0 <= a < n and 0 <= b < n and grid[a][b] == i:
                    found = True
                    x, y = a, b
                    break
            if not found:
                return False
        return True