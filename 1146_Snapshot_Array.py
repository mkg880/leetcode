import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.changes = [[] for _ in range(length)]
        self.curr = 0
        self.changed = {}

    def set(self, index: int, val: int) -> None:
        self.changed[index] = val

    def snap(self) -> int:
        ret = self.curr
        for key in self.changed:
            self.changes[key].append([ret, self.changed[key]])
        self.changed = {}
        self.curr += 1
        return ret

    def get(self, index: int, snap_id: int) -> int:
        arr = self.changes[index]
        idx = bisect.bisect_left(arr, snap_id, key=lambda x: x[0])
        if idx == len(arr) or arr[idx][0] > snap_id:
            idx -= 1
        return 0 if idx == -1 else arr[idx][1]



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)