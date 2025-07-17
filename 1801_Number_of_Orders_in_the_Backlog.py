class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        minHeap = []
        maxHeap = []
        res = 0
        mod = 10 ** 9 + 7
        for price, amount, kind in orders:
            (popping_heap, pushing_heap) = (minHeap, maxHeap) if kind == 0 else (maxHeap, minHeap)
            neg = 1 if kind == 0 else -1
            while popping_heap and amount:
                p, a = popping_heap[0]
                p *= neg
                (buyPrice, sellPrice) = (price, p) if kind == 0 else (p, price)
                if buyPrice < sellPrice:
                    break
                else:
                    if a > amount:
                        popping_heap[0][1] -= amount
                        res -= amount
                        if res < 0:
                            res += mod
                        amount = 0
                    else:
                        amount -= a
                        res -= a
                        if res < 0:
                            res += mod
                        heappop(popping_heap)
            if amount:
                price *= -neg
                heappush(pushing_heap, [price, amount])
            res += amount
            res %= mod
        return res