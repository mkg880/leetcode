class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for size in range(1, n+1):
            i, j = 0, size-1
            while j < n:
                turn = (i+j) % 2
                if turn:
                    dp[i][j] = max(piles[i] + dp[i+1][j], piles[j] + dp[i][j-1])
                else:
                    dp[i][j] = min(dp[i+1][j] - piles[i], dp[i][j-1] - piles[j])
                i += 1
                j += 1
        return dp[0][n-1] > 0