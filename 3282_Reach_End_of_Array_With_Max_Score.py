class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        res = 0
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[prev]:
                res += (i - prev) * nums[prev]
                prev = i
        if prev != len(nums) - 1:
            res += (len(nums) - 1 - prev) * nums[prev]
        return res