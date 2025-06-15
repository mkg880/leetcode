class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            disc = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    disc = prices[j]
                    break
            res.append(prices[i] - disc)
        return res