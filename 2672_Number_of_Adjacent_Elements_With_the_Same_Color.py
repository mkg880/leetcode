class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        m = {}
        colors = [0] * n
        curr = 0
        res = []
        for idx, color in queries:
            if colors[idx]:
                m[colors[idx]].remove(idx)
                if idx+1 in m[colors[idx]]:
                    curr -= 1
                if idx-1 in m[colors[idx]]:
                    curr -= 1
            colors[idx] = color
            if color not in m:
                m[color] = set()
            m[color].add(idx)
            if idx+1 in m[color]:
                curr += 1
            if idx-1 in m[color]:
                curr += 1
            res.append(curr)
        return res