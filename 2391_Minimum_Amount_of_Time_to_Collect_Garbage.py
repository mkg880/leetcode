from typing import Counter
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        lasts = [-1, -1, -1]
        res = 0
        for i, s in enumerate(garbage):
            res += len(s)
            c = Counter(s)
            for j, ch in enumerate(['M', 'P', 'G']):
                if ch in c:
                    lasts[j] = i-1
        c = Counter(lasts)
        tot = 0
        for i, val in enumerate(travel):
            tot += val
            if i in c:
                res += tot * c[i]
        return res
