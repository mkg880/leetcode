class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        prev = bottom-1
        res = 0
        for val in special:
            res = max(res, val - prev - 1)
            prev = val
        return max(res, top - prev)