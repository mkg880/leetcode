class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [0] * (time+1)
        for start, end in clips:
            start = min(start, time)
            end = min(end, time)
            dp[start] = max(dp[start], end)
        curr, next, res = dp[0], -1, 1
        if curr == time:
            return res
        for i in range(time+1):
            next = max(next, dp[i])
            if curr == i:
                curr = next
                res += 1
            if curr == time:
                return res
        return -1