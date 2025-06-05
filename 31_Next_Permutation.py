class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        idx = -1
        while i >= 0:
            if nums[i] < nums[i+1]:
                idx = i
                break
            i -= 1
        if idx >= 0:
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] > nums[idx]:
                    idx2 = j
                    break
            nums[idx], nums[j] = nums[j], nums[idx]
        start = idx+1
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        