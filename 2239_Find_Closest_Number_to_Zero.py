class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_abs, min_val = float('inf'), float('inf')
        for val in nums:
            a = abs(val)
            if a < min_abs or (a == min_abs and val > min_val):
                min_abs = a
                min_val = val
        return min_val