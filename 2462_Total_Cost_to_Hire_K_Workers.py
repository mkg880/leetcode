import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        n = len(costs)
        for i in range(candidates):
            heapq.heappush(heap, (costs[i], i, 1))
            if n - i - 1 >= candidates:
                heapq.heappush(heap, (costs[n-i-1], n-i-1, -1))
        l, r = candidates, n - candidates - 1
        res = 0
        for _ in range(k):
            cost, _, d = heapq.heappop(heap)
            res += cost
            idx = l if d == 1 else r
            if l <= r:
                heapq.heappush(heap, (costs[idx], idx, d))
            if d == 1:
                l += 1
            else:
                r -= 1
        return res