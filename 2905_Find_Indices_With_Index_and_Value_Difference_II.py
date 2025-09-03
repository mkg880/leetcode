class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min_idx, max_idx = 0, 0
        for i in range(indexDifference, len(nums)):
            idx = i - indexDifference
            if nums[idx] > nums[max_idx]:
                max_idx = idx
            if nums[idx] < nums[min_idx]:
                min_idx = idx
            if nums[max_idx] - nums[i] >= valueDifference:
                return [i, max_idx]
            if nums[i] - nums[min_idx] >= valueDifference:
                return [i, min_idx]
        return [-1, -1]