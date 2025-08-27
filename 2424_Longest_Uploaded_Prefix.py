import heapq
class LUPrefix:

    def __init__(self, n: int):
        self.heap = list(range(1, n+2))
        heapq.heapify(self.heap)
        self.uploaded = set()

    def upload(self, video: int) -> None:
        self.uploaded.add(video)

    def longest(self) -> int:
        while self.heap[0] in self.uploaded:
            heapq.heappop(self.heap)
        return self.heap[0] - 1


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()