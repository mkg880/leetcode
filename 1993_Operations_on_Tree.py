from collections import deque


class LockingTree:

    def __init__(self, parent: List[int]):
        self.desc = {}
        for c, p in enumerate(parent):
            self.desc[p] = self.desc.get(p, []) + [c]
        self.locks = [None] * len(parent)
        self.parent = parent

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] is None:
            self.locks[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == user:
            self.locks[num] = None
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.locks[num] is not None:
            return False
        p = self.parent[num]
        while p != -1:
            if self.locks[p] is not None:
                return False
            p = self.parent[p]
        found = False
        q = deque([num])
        arr = []
        while q:
            x = q.popleft()
            arr.append(x)
            if self.locks[x] is not None:
                found = True
            for d in self.desc.get(x, []):
                q.append(d)
        if not found:
            return False
        for x in arr:
            self.locks[x] = None
        self.locks[num] = user
        return True
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)