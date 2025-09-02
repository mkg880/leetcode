class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        def possible(val):
            cnt = 0
            i = 0
            while i < n-1:
                if nums[i+1] - nums[i] <= val:
                    cnt += 1
                    i += 1
                i += 1
            return cnt >= p
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo