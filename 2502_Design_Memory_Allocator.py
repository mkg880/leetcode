import bisect
class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.intervals = []
        self.m = {}

    def allocate(self, size: int, mID: int) -> int:
        prev_end = 0
        for i, (start, end) in enumerate(self.intervals):
            if start - prev_end >= size:
                self.intervals.insert(i, (prev_end, prev_end + size))
                if mID not in self.m:
                    self.m[mID] = set()
                self.m[mID].add((prev_end, prev_end + size))
                return prev_end
            prev_end = end
        if self.n - prev_end >= size:
            self.intervals.append((prev_end, prev_end + size))
            if mID not in self.m:
                self.m[mID] = set()
            self.m[mID].add((prev_end, prev_end + size))
            return prev_end
        return -1
    
    def freeMemory(self, mID: int) -> int:
        temp = []
        remove = self.m.get(mID, set())
        for i in self.intervals:
            if i not in remove:
                temp.append(i)
        self.intervals = temp
        self.m[mID] = set()
        return sum(end - start for start, end in remove)


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)