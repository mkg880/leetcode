class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(x + nums2[0], 0) for x in nums1]
        heapify(heap)
        res = []
        while k > 0:
            total, idx = heappop(heap)
            b = nums2[idx]
            a = total - b
            res.append([a, b])
            if idx + 1 < len(nums2):
                heappush(heap, (a + nums2[idx+1], idx+1))
            k -= 1
        return res
