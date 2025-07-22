class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        sorted_times = sorted([(t, i) for i, t in enumerate(times)])
        curr = 0
        chairs = []
        leaving = []
        for (a, l), i in sorted_times:
            while leaving and leaving[0][0] <= a:
                t, c = heappop(leaving)
                heappush(chairs, c)
            if chairs:
                val = heappop(chairs)
            else:
                val = curr
                curr += 1
            heappush(leaving, [l, val])
            if i == targetFriend:
                return val