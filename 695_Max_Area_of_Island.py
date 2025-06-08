class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i, j):
            if (i, j) in visited:
                return 0
            cnt = 1
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                visited.add((a, b))
                for c, d in directions:
                    e = a + c
                    f = b + d
                    if (e, f) not in visited and e >= 0 and e < len(grid) and f >= 0 and f < len(grid[e]) and grid[e][f] == 1:
                        visited.add((e, f))
                        stack.append((e, f))
                        cnt += 1
            return cnt
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
                    print(i, j, res)
        return res