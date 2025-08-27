class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        m = {}
        res, max_val = 0, 0
        for i, val in enumerate(edges):
            m[val] = m.get(val, 0) + i
            if m[val] > max_val or (m[val] == max_val and val < res):
                max_val = m[val]
                res = val
        return res