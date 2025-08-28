import heapq
from math import ceil
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap, -x)
        res = 0
        for _ in range(k):
            val = -heapq.heappop(heap)
            res += val
            heapq.heappush(heap, -ceil(val / 3))
        return res