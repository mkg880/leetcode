class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        cnt = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            dp[i][0] = matrix[i][0]
            cnt += dp[i][0]
        for j in range(1, n):
            dp[0][j] = matrix[0][j]
            cnt += dp[0][j]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                cnt += dp[i][j]
        return cnt