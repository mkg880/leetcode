class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        elif len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            return -1
        low = 0
        high = len(nums) - 1
        if nums[0] > nums[-1]:
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    pivot = mid+1
                    break
                elif nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                    pivot = mid
                    break
                elif nums[mid] < nums[-1]:
                    high = mid - 1
                else:
                    low = mid + 1
            if nums[pivot] == target:
                return pivot
            elif target > nums[-1]:
                low = 0
                high = pivot - 1
            else:
                low = pivot + 1
                high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
            