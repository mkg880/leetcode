class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        res = float('inf')
        def f(i, j):
            nonlocal res
            a, b = timePoints[i].split(':')
            c, d = timePoints[j].split(':')
            a, b, c, d = int(a), int(b), int(c), int(d)
            val1 = (c-a) * 60 + d - b
            a += 24
            val2 = (a-c) * 60 + b - d
            val = min(val1, val2)
            res = min(val, res)
        for i in range(len(timePoints) - 1):
            f(i, i+1)
        f(0, len(timePoints) - 1)
        return res
