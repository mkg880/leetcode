class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        rise, run = None, None
        res = 0
        stockPrices.sort()
        x1, y1 = stockPrices[0]
        for i in range(1, len(stockPrices)):
            x2, y2 = stockPrices[i]
            if rise is None or (y2-y1) * run != (x2 - x1) * rise:
                res += 1
            rise, run = y2-y1, x2-x1
            x1, y1 = x2, y2
        return res