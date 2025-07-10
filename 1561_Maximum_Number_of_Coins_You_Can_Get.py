class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        alice, me, bob = n-1, n-2, 0
        res = 0
        while bob < me:
            res += piles[me]
            bob += 1
            me -= 2
            alice -= 2
        return res