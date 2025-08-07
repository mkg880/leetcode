class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        start = None
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start is not None:
                break
        stack = [start]
        q = deque()
        while stack:
            i, j = stack.pop()
            if not 0 <= i < n or not 0 <= j < n or grid[i][j] != 1:
                continue
            grid[i][j] = 2
            for di, dj in directions:
                stack.append((i+di, j+dj))
                q.append((i+di, j+dj, 0))
        vis = set()
        while q:
            i, j, d = q.popleft()
            if (i, j) in vis or not 0 <= i < n or not 0 <= j < n or grid[i][j] == 2:
                continue
            vis.add((i, j))
            if grid[i][j] == 1:
                return d
            for di, dj in directions:
                q.append((i+di, j+dj, d+1))