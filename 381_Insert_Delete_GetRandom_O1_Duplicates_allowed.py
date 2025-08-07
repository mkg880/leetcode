class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.m = {}

    def insert(self, val: int) -> bool:
        ret = False
        if val not in self.m:
            self.m[val] = set()
            ret = True
        self.m[val].add(len(self.list))
        self.list.append(val)
        return ret

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        prev = len(self.list) - 1
        if self.list[-1] == val:
            self.list.pop()
            self.m[val].remove(prev)
            if len(self.m[val]) == 0:
                del self.m[val]
            return True
        idx = next(iter(self.m[val]))
        self.list[idx], self.list[prev] = self.list[prev], self.list[idx]
        self.m[self.list[idx]].remove(prev)
        self.m[self.list[idx]].add(idx)
        self.m[val].remove(idx)
        self.list.pop()
        if len(self.m[val]) == 0:
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