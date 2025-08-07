class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        m = {}
        n = len(intervals)
        for i in range(n):
            start = intervals[i][0]
            m[start] = i
        arr = sorted(intervals)
        res = []
        for _, end in intervals:
            idx = bisect_left(arr, end, key=lambda x: x[0])
            if idx == n:
                val = -1
            else:
                start, _ = arr[idx]
                val = m[start]
            res.append(val)
        return res