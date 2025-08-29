import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)
        marked = set()
        res = 0
        while heap:
            score, idx = heapq.heappop(heap)
            if idx in marked:
                continue
            res += score
            marked.update([idx-1, idx+1])
        return res