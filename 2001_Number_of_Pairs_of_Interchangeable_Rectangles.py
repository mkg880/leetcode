class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        m = {}
        res = 0
        for w, h in rectangles:
            ratio = w / h
            prev = m.get(ratio, 0)
            res += prev
            m[ratio] = prev + 1
        return res