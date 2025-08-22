class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr = 0
        l, h = float('inf'), float('-inf')
        for val in differences:
            curr += val
            l = min(l, curr)
            h = max(h, curr)
        lo = max(lower, lower - l)
        hi = min(upper, upper - h)
        return max(hi - lo + 1, 0)