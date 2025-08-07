class RandomizedSet:

    def __init__(self):
        self.list = []
        self.m = {}

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        self.m[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        idx = self.m[val]
        self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
        self.m[self.list[idx]] = idx
        self.list.pop()
        del self.m[val]
        return True

    def getRandom(self) -> int:
        n = len(self.list)
        i = randint(0, n-1)
        return self.list[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()