class Bitset:

    def __init__(self, size: int):
        self.arr = [False] * size
        self.cnt = 0
        self.flipped = False
        self.size = size

    def fix(self, idx: int) -> None:
        if self.flipped == self.arr[idx]:
            self.arr[idx] = not self.arr[idx]
            self.cnt += 1

    def unfix(self, idx: int) -> None:
        if self.flipped != self.arr[idx]:
            self.arr[idx] = not self.arr[idx]
            self.cnt -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.cnt = self.size - self.cnt

    def all(self) -> bool:
        return self.cnt == self.size

    def one(self) -> bool:
        return self.cnt > 0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        return ''.join(['0' if self.flipped == self.arr[i] else '1' for i in range(self.size)])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()