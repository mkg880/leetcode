class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        m = {}
        res = 0
        for t in hours:
            mod = t % 24
            res += m.get((24 - mod) % 24, 0)
            m[mod] = m.get(mod, 0) + 1
        return res