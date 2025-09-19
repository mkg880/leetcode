from math import ceil
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        def possible(k):
            prev = start[0]
            for val in start[1:]:
                prev = max(prev + k, val)
                if prev > val + d:
                    return False
            return True
        lo, hi = 0, start[-1] - start[0] + d
        while lo < hi:
            mid = ceil((lo + hi) / 2)
            if possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo