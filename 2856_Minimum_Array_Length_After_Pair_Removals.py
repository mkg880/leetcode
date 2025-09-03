from math import ceil
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) // 2
        while lo < hi:
            mid = ceil((lo + hi) / 2)
            if all(nums[i] < nums[-mid+i] for i in range(mid)):
                lo = mid
            else:
                hi = mid-1
        return len(nums) - 2 * lo