class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        adj = [[i+1] if i < n-1 else [] for i in range(n)]
        for a, b in queries:
            adj[a].append(b)
            dp = [0] * n
            for x in range(n-2, -1, -1):
                dp[x] = min(dp[neighbor] + 1 for neighbor in adj[x])
            res.append(dp[0])
        return res