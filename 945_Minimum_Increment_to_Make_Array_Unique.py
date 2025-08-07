class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                new_val = nums[i-1] + 1
                res += new_val - nums[i]
                nums[i] = new_val
        return res