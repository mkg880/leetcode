import heapq
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        heaps = []
        for row in nums:
            heaps.append([-x for x in row])
            heapq.heapify(heaps[-1])
        res = 0
        n = len(nums[0])
        for _ in range(n):
            curr = 0
            for heap in heaps:
                curr = max(curr, -heapq.heappop(heap))
            res += curr
        return res