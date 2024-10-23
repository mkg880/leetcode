class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n-2, -1, -1):
            val = min(i + nums[i] + 1, n)
            m = float('inf')
            for j in range(i+1, val):
                m = min(dp[j], m)
            dp[i] = 1 + m
        return dp[0]