import heapq
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = sum(nums)
        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)
        marked = set()
        res = []
        for i, k in queries:
            if i not in marked:
                marked.add(i)
                total -= nums[i]
            cnt = 0
            while heap and cnt < k:
                _, idx = heapq.heappop(heap)
                if idx not in marked:
                    cnt += 1
                    marked.add(idx)
                    total -= nums[idx]
            res.append(total)
        return res