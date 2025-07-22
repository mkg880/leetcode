class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def cmp(item):
            return item[0]
        items.sort(key=cmp)
        ranges = [[0, 0, float('inf')]]
        for p, b in items:
            prev = ranges[-1]
            if b > prev[1]:
                ranges[-1][2] = p
                ranges.append([p, b, float('inf')])
        res = []
        for q in queries:
            idx = bisect_right(ranges, q, key=lambda x: x[0]) - 1
            res.append(ranges[idx][1])
        return res