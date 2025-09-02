class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        return len(nums) <= 2 or any(nums[i] + nums[i+1] >= m for i in range(len(nums) - 1))