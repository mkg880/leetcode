from math import ceil
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        def possible(val):
            cnt = 1
            prev = price[0]
            for i in range(1, n):
                if price[i] - prev >= val:
                    cnt += 1
                    prev = price[i]
            return cnt >= k
        lo, hi = 0, price[-1] - price[0]
        while lo < hi:
            mid = ceil((lo + hi) / 2)
            if possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo