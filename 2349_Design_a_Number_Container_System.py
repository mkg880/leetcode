import heapq


class NumberContainers:

    def __init__(self):
        self.i_to_n = {}
        self.n_to_i = {}

    def change(self, index: int, number: int) -> None:
        self.i_to_n[index] = number
        if number not in self.n_to_i:
            self.n_to_i[number] = []
        heapq.heappush(self.n_to_i[number], index)

    def find(self, number: int) -> int:
        heap = self.n_to_i.get(number, [])
        while heap:
            idx = heapq.heappop(heap)
            if self.i_to_n.get(idx, -1) == number:
                heapq.heappush(heap, idx)
                return idx
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)