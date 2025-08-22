import bisect
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        m = {}
        for l, h in rectangles:
            if h not in m:
                m[h] = []
            bisect.insort(m[h], l)
        res = []
        for x, y in points:
            cnt = 0
            for h in range(y, 101):
                if h not in m:
                    continue
                cnt += len(m[h]) - bisect.bisect_left(m[h], x)
            res.append(cnt)
        return res