class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x, y = p
            heappush(heap, (x**2 + y**2, p))
        return [heappop(heap)[1] for i in range(k)]
        