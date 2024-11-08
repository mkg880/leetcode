class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnt = [[s.count("0"), s.count("1")] for s in strs]
        @cache
        def rec(a, b, i):
            if a < 0 or b < 0:
                return float('-inf')
            if i == len(strs):
                return 0
            z, o = cnt[i]
            return max(rec(a, b, i+1), 1 + rec(a - z, b - o, i+1))
        return rec(m, n, 0)