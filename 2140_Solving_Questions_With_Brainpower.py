class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            p, b = questions[i]
            solvable = b + i + 1
            if solvable < n:
                p += dp[solvable]
            skip = dp[i+1] if i < n-1 else 0
            dp[i] = max(skip, p)
        return dp[0]