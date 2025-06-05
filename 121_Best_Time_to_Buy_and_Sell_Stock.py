class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        m = float('inf')
        for val in prices:
            res = max(val-m, res)
            m = min(val, m)
        return res