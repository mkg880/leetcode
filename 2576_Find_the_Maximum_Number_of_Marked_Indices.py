from math import ceil
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        lo, hi = 0, len(nums) // 2
        while lo < hi:
            mid = ceil((lo + hi) / 2)
            if all(2 * nums[i] <= nums[-mid+i] for i in range(mid)):
                lo = mid
            else:
                hi = mid - 1
        return lo*2