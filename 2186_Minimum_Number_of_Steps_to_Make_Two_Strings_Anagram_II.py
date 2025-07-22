class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        res = 0
        for key in c1.keys() | c2.keys():
            res += abs(c1.get(key, 0) - c2.get(key, 0))
        return res