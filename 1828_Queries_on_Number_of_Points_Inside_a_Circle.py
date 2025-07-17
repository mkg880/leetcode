class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for x, y, r in queries:
            cnt = 0
            for a, b in points:
                dist_sq = (x - a) ** 2 + (y - b) ** 2
                if dist_sq <= r ** 2:
                    cnt += 1
            res.append(cnt)
        return res