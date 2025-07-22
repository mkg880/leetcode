class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapify(heap)
        res = 0
        for i in range(k):
            if not heap:
                return res
            x = -heappop(heap)
            x = ceil(x / 2)
            if x >= 1:
                heappush(heap, -x)
        return res - sum(heap)