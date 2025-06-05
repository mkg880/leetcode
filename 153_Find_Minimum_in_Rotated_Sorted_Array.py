class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        hi = len(nums) - 1
        while low < hi:
            mid = (low + hi) // 2
            if nums[mid] < nums[-1]:
                hi = mid
            else:
                low = mid + 1
        return nums[low]