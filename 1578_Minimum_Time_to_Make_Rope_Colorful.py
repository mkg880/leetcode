class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        n = len(neededTime)
        res = 0
        while i < n:
            j = i + 1
            max_val, total = neededTime[i], neededTime[i]
            while j < n and colors[j] == colors[i]:
                max_val = max(max_val, neededTime[j])
                total += neededTime[j]
                j += 1
            if j - i > 1:
                res += total - max_val
            i = j
        return res