class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[] for row in triangle]
        dp[0].append(triangle[0][0])
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                l = float('inf')
                r = float('inf')
                if j - 1 >= 0:
                    l = dp[i-1][j-1]
                if j < len(dp[i-1]):
                    r = dp[i-1][j]
                dp[i].append(triangle[i][j] + min(l, r))
        return min(dp[len(triangle) - 1])