class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s0, s1, s2 = 0, -prices[0], float('-inf')
        for p in prices[1:]:
            a, b, c = s0, s1, s2
            s0 = max(a, c)
            s1 = max(b, a - p)
            s2 = b + p
        return max(s0, s1, s2)