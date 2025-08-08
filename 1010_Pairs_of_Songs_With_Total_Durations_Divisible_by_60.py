class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        m = {}
        res = 0
        for t in time:
            mod = t % 60
            res += m.get((60 - mod) % 60, 0)
            m[mod] = m.get(mod, 0) + 1
        return res