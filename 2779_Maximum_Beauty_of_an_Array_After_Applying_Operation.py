from math import ceil
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mid = ceil((lo + hi) / 2)
            if any(nums[i+mid-1] - nums[i] <= 2 * k for i in range(n-mid+1)):
                lo = mid
            else:
                hi = mid - 1
        return lo