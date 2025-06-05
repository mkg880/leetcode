class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for val in row] for row in obstacleGrid]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if (i == 0 and j == 0) or obstacleGrid[i][j] == 1:
                    continue
                if i-1 >= 0 and obstacleGrid[i-1][j] == 0:
                    dp[i][j] += dp[i-1][j]
                if j-1 >= 0 and obstacleGrid[i][j-1] == 0:
                    dp[i][j] += dp[i][j-1]
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]