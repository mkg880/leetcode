class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for i in range(len(grid))]
        for j in range(len(grid[0]) - 2, -1, -1):
            for i in range(len(grid)):
                if grid[i][j+1] > grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i][j+1] + 1)
                if i - 1 >= 0 and grid[i-1][j+1] > grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j+1] + 1)
                if i+1 < len(grid) and grid[i+1][j+1] > grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j+1] + 1)
        res = 0
        for i in range(len(grid)):
            res = max(res, dp[i][0])
        return res