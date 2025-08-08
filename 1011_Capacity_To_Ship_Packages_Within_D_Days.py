class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(x):
            curr = weights[0]
            if curr > x:
                return False
            cnt = 1
            for val in weights[1:]:
                if val > x:
                    return False
                if curr + val > x:
                    cnt += 1
                    curr = val
                else:
                    curr += val
            return cnt <= days
        lo = 1
        hi = sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid+1
        return lo