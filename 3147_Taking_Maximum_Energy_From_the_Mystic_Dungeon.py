class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * (n+k)
        res = float('-inf')
        for i in range(n-1, -1, -1):
            dp[i] = energy[i] + dp[i+k]
            res = max(res, dp[i])
        return res