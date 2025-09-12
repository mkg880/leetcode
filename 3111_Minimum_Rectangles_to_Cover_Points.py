class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        x = sorted([p[0] for p in points])
        end = -1
        res = 0
        for val in x:
            if val > end:
                res += 1
                end = val + w
        return res