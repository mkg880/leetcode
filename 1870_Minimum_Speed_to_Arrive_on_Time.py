from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        def possible(speed):
            t = 0
            for d in dist:
                t = ceil(t)
                t += d / speed
                if t > hour:
                    return False
            return True
        lo, hi = 1, 10 ** 7
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo