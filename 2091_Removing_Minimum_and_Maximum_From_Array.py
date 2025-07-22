class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_val, min_idx = float('inf'), -1
        max_val, max_idx = float('-inf'), -1
        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
                min_idx = i
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i
        first, second = min(min_idx, max_idx), max(min_idx, max_idx)
        l, r, diff = first + 1, n - second, second - first
        return min(l+r, l+diff, r+diff)