from heapq import heappop, heappush
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        start_day = events[0][0]
        end_day = max(x[1] for x in events)
        heap = []
        res = 0
        i = 0
        for day in range(start_day, end_day+1):
            while i < len(events) and events[i][0] <= day:
                heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heappop(heap)
            if heap:
                res += 1
                heappop(heap)
        return res
        