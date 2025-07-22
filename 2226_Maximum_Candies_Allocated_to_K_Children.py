class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(val):
            cnt = 0
            for c in candies:
                cnt += c // val
            return cnt >= k
        lo = 0
        hi = max(candies)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo