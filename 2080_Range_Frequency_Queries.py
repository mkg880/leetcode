import bisect
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.m = {}
        for i in range(len(arr)):
            if arr[i] not in self.m:
                self.m[arr[i]] = []
            self.m[arr[i]].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.m:
            return 0
        indices = self.m[value]
        l = bisect.bisect_left(indices, left)
        if l == len(indices):
            return 0
        r = bisect.bisect_right(indices, right)
        if r == 0:
            return 0
        return r-l


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)