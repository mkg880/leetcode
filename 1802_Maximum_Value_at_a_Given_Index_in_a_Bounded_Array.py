from math import ceil
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        r = n - index - 1
        def possible(val):
            d = val
            m = min(index, val-1)
            d += m * val - m * (m + 1) // 2 + (index - m)
            m = min(r, val-1)
            d += m * val - m * (m + 1) // 2 + (r - m)
            return d <= maxSum
        lo, hi = 1, maxSum
        while lo < hi:
            mid = ceil((lo + hi) / 2)
            if possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo