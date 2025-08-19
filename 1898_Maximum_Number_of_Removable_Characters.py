from math import ceil


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def possible(k):
            indices = set(removable[:k])
            i, j = 0, 0
            while i < len(s) and j < len(p):
                if i not in indices and s[i] == p[j]:
                    j += 1
                i += 1
            return j == len(p)
        
        lo, hi = 0, len(removable)
        while lo < hi:
            mid = ceil((lo + hi) / 2)
            if possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
                