class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr = encoding
        self.curr = 0

    def next(self, n: int) -> int:
        if self.curr == len(self.arr):
            return -1
        if self.arr[self.curr] >= n:
            self.arr[self.curr] -= n
            ret = self.arr[self.curr + 1]
            if self.arr[self.curr] == 0:
                self.curr += 2
            return ret
        rem = n - self.arr[self.curr]
        self.curr += 2
        return self.next(rem)
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)