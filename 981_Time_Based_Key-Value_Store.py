from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key] = self.m.get(key, []) + [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ''
        arr = self.m[key]
        idx = bisect_left(arr, timestamp, key=lambda x: x[0])
        if idx < len(arr) and arr[idx][0] == timestamp:
            return arr[idx][1]
        if idx == 0:
            return ''
        return arr[idx-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)