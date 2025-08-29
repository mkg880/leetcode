import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        arr = sorted(list(zip(nums1, nums2)), key=lambda x: -x[1])
        heap = []
        total = 0
        res = 0
        for i in range(n):
            total += arr[i][0]
            heapq.heappush(heap, arr[i][0])
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, total * arr[i][1])
        return res