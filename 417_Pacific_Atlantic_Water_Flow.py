class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(heights)
        n = len(heights[0])
        def dfs(i, j):
            pac = False
            atl = False
            visited = set()
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                if (a, b) in visited:
                    continue
                visited.add((a, b))
                if a == 0 or b == 0:
                    pac = True
                if a == m - 1 or b == n - 1:
                    atl = True
                if pac and atl:
                    return True
                for c, d in directions:
                    e, f = a + c, b + d
                    if e >= 0 and e < m and f >= 0 and f < n and heights[e][f] <= heights[a][b]:
                        stack.append((e, f))
            return False
        res = []
        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    res.append([i, j])
        return res