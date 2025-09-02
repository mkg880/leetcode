class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        r, l = {}, {}
        for i in range(m):
            for j in range(n):
                if j-i not in r:
                    r[j-i] = {}
                    l[j-i] = {}
                r[j-i][grid[i][j]] = r[j-i].get(grid[i][j], 0) + 1
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r[j-i][grid[i][j]] -= 1
                if not r[j-i][grid[i][j]]: del r[j-i][grid[i][j]]
                res[i][j] = abs(len(r[j-i]) - len(l[j-i]))
                l[j-i][grid[i][j]] = l[j-i].get(grid[i][j], 0) + 1
        return res