class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        indices = []
        while i < len(nums):
            if i < len(nums) - 1 and nums[i] == nums[i+1]:
                nums[i] *= 2
                if nums[i] != 0:
                    indices.append(i)
                i += 2
            else:
                if nums[i] != 0:
                    indices.append(i)
                i += 1
        idx = 0
        while idx < len(indices):
            nums[idx] = nums[indices[idx]]
            idx += 1
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
        return nums