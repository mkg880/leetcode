class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5:
            return 0
        nums.sort()
        res = float('inf')
        for l in range(4):
            res = min(res, nums[l + n - 4] - nums[l])
        return res