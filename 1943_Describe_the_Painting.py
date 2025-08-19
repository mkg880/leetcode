class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        m = {}
        for start, end, color in segments:
            m[start] = m.get(start, 0) + color
            m[end] = m.get(end, 0) - color
        res = []
        prev, curr = None, 0
        for key in sorted(m.keys()):
            if curr != 0:
                res.append([prev, key, curr])
            curr += m[key]
            prev = key
        return res
