class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        counts = {}
        res = []
        for x, y in queries:
            if x in colors:
                counts[colors[x]] -= 1
                if counts[colors[x]] == 0:
                    del counts[colors[x]]
            colors[x] = y
            counts[y] = counts.get(y, 0) + 1
            res.append(len(counts))
        return res