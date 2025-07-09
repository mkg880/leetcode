class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def cmp(x):
            a, b, c = x
            return [b, c, a]
        trips.sort(key=cmp)
        heap = []
        curr = 0
        for n, f, t in trips:
            while heap and heap[0][0] <= f:
                _, x = heappop(heap)
                curr -= x
            curr += n
            if curr > capacity:
                return False
            heappush(heap, [t, n])
        return True