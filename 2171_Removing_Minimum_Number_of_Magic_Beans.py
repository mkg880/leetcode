class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        total = sum(beans)
        beans.sort()
        res = float('inf')
        bef = 0
        for i, val in enumerate(beans):
            total -= val
            amt = bef + (total - (n-i-1) * val)
            bef += val
            res = min(res, amt)
        return res