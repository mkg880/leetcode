import bisect
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            l = bisect.bisect_left(nums, lower - nums[i], lo=i+1)
            if l == len(nums):
                continue
            if nums[l] < lower - nums[i]:
                l += 1
            r = bisect.bisect_left(nums, upper - nums[i] + 1, lo=i+1) - 1
            res += r - l + 1
        return res
        