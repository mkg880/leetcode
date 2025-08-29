class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        j = 0
        dp = [0] * (n+1)
        res = 0
        for i in range(n):
            while prizePositions[j] < prizePositions[i] - k:
                j += 1
            dp[i+1] = max(dp[i], i-j+1)
            res = max(res, dp[j] + i - j + 1)
        return res