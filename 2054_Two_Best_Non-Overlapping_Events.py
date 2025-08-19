import bisect
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        starts = sorted([[s, v] for s, _, v in events], key=lambda x: x[0])
        ends = sorted([[e, v] for _, e, v in events], key=lambda x: x[0])
        start_vals = [0] * n
        curr = 0
        for i in range(n-1, -1, -1):
            curr = max(curr, starts[i][1])
            start_vals[i] = curr
        end_vals = [0] * n
        curr = 0
        for i in range(n):
            curr = max(curr, ends[i][1])
            end_vals[i] = curr
        res = 0
        for start, end, value in events:
            idx = bisect.bisect_right(ends, start-1, key=lambda x: x[0])
            pre = 0 if idx == 0 else end_vals[idx-1]
            idx = bisect.bisect_left(starts, end+1, key=lambda x: x[0])
            post = 0 if idx == n else start_vals[idx]
            res = max(res, value + max(pre, post))
        return res