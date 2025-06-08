from statistics import median
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        m = median(nums)
        return int(sum([abs(n - m) for n in nums]))