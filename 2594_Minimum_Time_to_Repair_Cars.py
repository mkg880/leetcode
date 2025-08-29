from math import floor
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        lo, hi = 1, min(ranks) * cars ** 2
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(floor((mid / rank) ** 0.5) for rank in ranks) >= cars:
                hi = mid
            else:
                lo = mid + 1
        return lo