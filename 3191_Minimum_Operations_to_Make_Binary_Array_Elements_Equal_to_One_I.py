class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] % 2 == 0:
                res += 1
                nums[i+1] += 1
                nums[i+2] += 1
        return -1 if any(nums[i] % 2 == 0 for i in range(len(nums) - 2, len(nums))) else res