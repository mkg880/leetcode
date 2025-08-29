import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        n = len(speed)
        arr = sorted(list(zip(speed, efficiency)), key=lambda x: -x[1])
        heap = []
        total = 0
        res = 0
        for i in range(n):
            total += arr[i][0]
            heapq.heappush(heap, arr[i][0])
            if len(heap) > k:
                total -= heapq.heappop(heap)
            res = max(res, total * arr[i][1])
        return res % (10 ** 9 + 7)