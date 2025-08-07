class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        max_val = float('-inf')
        for i in range(2, len(nums)):
            max_val = max(max_val, nums[i-2])
            if nums[i] < max_val:
                return False
        return True