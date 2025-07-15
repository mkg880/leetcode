class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        res = 0
        for i, (a, d) in enumerate(zip(apples, days)):
            if a:
                heappush(heap, [i+d, a])
            while heap and heap[0][0] <= i:
                heappop(heap)
            if heap:
                res += 1
                heap[0][1] -= 1
                if heap[0][1] == 0:
                    heappop(heap)
        curr = len(apples)
        while heap:
            while heap and heap[0][0] <= curr:
                heappop(heap)
            if not heap:
                break
            val = min(heap[0][1], heap[0][0] - curr)
            curr += val
            res += val
            heappop(heap)
        return res