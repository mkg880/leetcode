class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1] + 1
        dp = [0] * last_day
        curr = 0
        for i in range(1, last_day):
            if i < days[curr]:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(0, i-1)] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
                curr += 1
        return dp[-1]