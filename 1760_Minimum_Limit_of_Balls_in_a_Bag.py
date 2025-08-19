from math import ceil
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def possible(penalty):
            ops = 0
            for x in nums:
                ops += ceil(x / penalty) - 1
            return ops <= maxOperations
        lo, hi = 1, 10 ** 9
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo  