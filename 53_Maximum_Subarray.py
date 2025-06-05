class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        m = nums[0]
        for i in range(1, len(nums)):
            m = max(m+nums[i], nums[i])
            res = max(m, res)
        return res