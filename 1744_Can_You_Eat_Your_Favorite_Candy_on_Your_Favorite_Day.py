class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        pre = [0] * len(candiesCount)
        curr = 0
        for i in range(len(candiesCount)):
            curr += candiesCount[i]
            pre[i] = curr
        res = []
        for candy, day, cap in queries:
            low = (pre[candy] - candiesCount[candy]) // cap
            hi = pre[candy] - 1
            res.append(day <= hi and day >= low)
        return res