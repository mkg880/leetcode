class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        start, end = intervals[0]
        for a, b in intervals:
            if a <= end:
                end = max(b, end)
            else:
                res.append([start, end])
                start, end = a, b
        res.append([start, end])
        return res