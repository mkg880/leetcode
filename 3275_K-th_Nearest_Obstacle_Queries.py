import heapq
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap = []
        res = []
        for x, y in queries:
            val = abs(x) + abs(y)
            if len(heap) == k and val < -heap[0]:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap, -val)
            res.append(-heap[0] if len(heap) == k else -1)
        return res