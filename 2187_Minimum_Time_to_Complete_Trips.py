class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def possible(val):
            total = sum([val // t for t in time])
            return total >= totalTrips
        lo = 1
        hi = min(time) * totalTrips
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo