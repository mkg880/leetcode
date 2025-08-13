class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        size = n - k
        res = 0
        for i in range(size):
            res += cardPoints[i]
        curr = res
        for i in range(k):
            curr -= cardPoints[i]
            curr += cardPoints[i+size]
            res = min(res, curr)
        return sum(cardPoints) - res