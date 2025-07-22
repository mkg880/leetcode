class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        curr = 0.0
        heap = [-x for x in nums]
        heapify(heap)
        cnt = 0
        while curr < target:
            val = -heappop(heap)
            half = val / 2
            curr += half
            heappush(heap, -half)
            cnt += 1
        return cnt