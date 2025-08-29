class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        b = set(banned)
        tot = 0
        for i in range(1, n+1):
            if i in b:
                continue
            tot += i
            if tot > maxSum:
                break
            res += 1
        return res