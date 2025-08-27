class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            l, r = max(0, idx - k), min(26, idx + k + 1)
            dp[idx] = max(dp[idx], max(dp[l:r]) + 1)
        return max(dp)