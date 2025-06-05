class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        hi = len(nums) - 1
        while low < hi:
            mid = (low + hi) // 2
            l = nums[mid-1] if mid - 1 >= 0 else float('-inf')
            r = nums[mid+1] if mid + 1 < len(nums) else float('-inf')
            if nums[mid] > l and nums[mid] > r:
                return mid
            elif nums[mid] < l:
                hi = mid-1
            else:
                low = mid+1
        return low