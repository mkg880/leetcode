class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_val, max_val = nums[0], nums[-1]
        res = max_val - min_val
        for i in range(1, len(nums)):
            curr = max(max_val - k, nums[i-1] + k) - min(min_val + k, nums[i] - k)
            res = min(res, curr)
        return res