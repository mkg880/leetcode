class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        minx = float('inf')
        miny = float('inf')
        maxx = float('-inf')
        maxy = float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    minx = min(minx, i)
                    miny = min(miny, j)
                    maxx = max(maxx, i)
                    maxy = max(maxy, j)
        return (maxx - minx + 1) * (maxy - miny + 1)