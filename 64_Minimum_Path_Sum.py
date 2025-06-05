class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for val in row] for row in grid]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                val = float('inf')
                if i - 1 >= 0:
                    val = dp[i-1][j]
                if j - 1 >= 0 and dp[i][j-1] < val:
                    val = dp[i][j-1]
                dp[i][j] = val + grid[i][j]
        return dp[len(dp) - 1][len(dp[0]) - 1]
                