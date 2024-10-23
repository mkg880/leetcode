class Solution:
    def find_index(self, arr, n, K):
        start = 0
        end = n - 1
        while start<= end:
            mid =(start + end)//2
            if arr[mid][0] == K:
                return mid
            elif arr[mid][0] < K:
                start = mid + 1
            else:
                end = mid-1
        return end + 1
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = self.find_index(intervals, len(intervals), newInterval[0])
        intervals.insert(idx, newInterval)
        start, end = idx, idx
        max_end = newInterval[1]
        while start >= 1 and intervals[start-1][1] >= intervals[start][0]:
            start -= 1
            max_end = max(intervals[start][1], max_end)
        while end < len(intervals) - 1 and intervals[end+1][0] <= intervals[idx][1]:
            end += 1
            max_end = max(intervals[end][1], max_end)
        res = []
        for i in range(start):
            res.append(intervals[i])
        res.append([intervals[start][0], max_end])
        for i in range(end+1, len(intervals)):
            res.append(intervals[i])
        return res
        