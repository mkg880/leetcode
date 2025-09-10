import heapq
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        res = []
        heap = []
        m = {}
        for n, f in zip(nums, freq):
            m[n] = max(m.get(n, 0) + f, 0)
            heapq.heappush(heap, (-m[n], n))
            x = 0
            while heap:
                amt, val = heap[0]
                if m[val] != -amt:
                    heapq.heappop(heap)
                else:
                    x = -amt
                    break
            res.append(x)
        return res