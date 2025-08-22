class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        res = float('inf')
        for h in range(100):
            if h * 60 > targetSeconds:
                break
            if h * 60 + 99 < targetSeconds:
                continue
            cost = 0
            seconds = targetSeconds - h * 60
            s = str(h) + f"{seconds:02d}" if h else str(seconds)
            curr = str(startAt)
            for c in s:
                if c != curr:
                    curr = c
                    cost += moveCost
                cost += pushCost
            res = min(res, cost)
        return res