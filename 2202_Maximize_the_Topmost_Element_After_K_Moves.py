class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k % 2 == 1 and len(nums) == 1:
            return -1
        arr = nums[:k+1]
        if 0 <= k - 1 < len(nums):
            arr.pop(k-1)
        return max(arr)