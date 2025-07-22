class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = sum(nums)
        swaps = ones - sum(nums[:ones])
        res = swaps
        for i in range(1, n):
            if nums[i-1] == 0:
                swaps -= 1
            last = (i + ones - 1) % n
            if nums[last] == 0:
                swaps += 1
            res = min(res, swaps)
        return res