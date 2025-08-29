class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def possible(val):
            cnt = 0
            i = 0
            while i < len(nums):
                if nums[i] <= val:
                    cnt += 1
                    i += 1
                i += 1
            return cnt >= k
        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo