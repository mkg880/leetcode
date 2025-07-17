class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        max_val = max(start, len(nums) - start - 1)
        for dist in range(max_val + 1):
            l, r = start - dist, start + dist
            if (l >= 0 and nums[l] == target) or (r < len(nums) and nums[r] == target):
                return dist