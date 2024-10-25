class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if(n % 2 == 0):
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        # dp = [0] * (n+2)
        # dp[1] = 0
        # for i in range(2, n+2):
        #     if i % 2 == 0:
        #         dp[i] = 1 + dp[i // 2]
        #         if dp[i] + 1 < dp[i-1]:
        #             dp[i-1] = dp[i] + 1
        #     else:
        #         dp[i] = 1 + dp[i-1]
        # return dp[n]