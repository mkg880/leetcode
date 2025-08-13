class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        res = n
        end = -1
        for i in range(n):
            if (i < n - 1 and intervals[i][0] == intervals[i+1][0]) or intervals[i][1] <= end:
                res -= 1
            end = max(end, intervals[i][1])
        return res
