class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        m = {}
        curr = 0
        res = 0
        for i in range(len(hours) + 1):
            if curr not in m:
                m[curr] = i
            if curr > 0:
                res = i
            res = max(res, i - m.get(curr-1, i))
            if i < len(hours):
                curr += 1 if hours[i] > 8 else -1
        return res