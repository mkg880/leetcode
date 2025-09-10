from heapq import heapify, heappop, heappush
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        cnt = 0
        while True:
            a = heappop(nums)
            if a >= k:
                return cnt
            b = heappop(nums)
            x, y = min(a, b), max(a, b)
            heappush(nums, x * 2 + y)
            cnt += 1