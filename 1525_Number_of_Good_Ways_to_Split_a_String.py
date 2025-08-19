from typing import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        r = Counter(s)
        l = {}
        res = 0
        for c in s:
            if len(r) == len(l):
                res += 1
            l[c] = l.get(c, 0) + 1
            r[c] -= 1
            if r[c] == 0:
                del r[c]
        return res