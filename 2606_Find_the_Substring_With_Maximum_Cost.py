class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        m = dict(zip(chars, vals))
        prev = 0
        res = 0
        for i in range(len(s)):
            cost = m.get(s[i], ord(s[i]) - ord('a') + 1)
            prev = max(0, prev + cost, cost)
            res = max(res, prev)
        return res