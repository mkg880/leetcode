class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 2, 2
        while i < len(nums):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k