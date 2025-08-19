import heapq
class StockPrice:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.m = {}
        self.latest = -1

    def update(self, timestamp: int, price: int) -> None:
        self.m[timestamp] = price
        self.latest = max(self.latest, timestamp)
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.m[self.latest]

    def maximum(self) -> int:
        while True:
            price, timestamp = heapq.heappop(self.max_heap)
            if self.m[timestamp] == -price:
                heapq.heappush(self.max_heap, (price, timestamp))
                return -price

    def minimum(self) -> int:
        while True:
            price, timestamp = heapq.heappop(self.min_heap)
            if self.m[timestamp] == price:
                heapq.heappush(self.min_heap, (price, timestamp))
                return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()