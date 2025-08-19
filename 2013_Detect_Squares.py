class DetectSquares:

    def __init__(self):
        self.m = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        self.m[(x, y)] = self.m.get((x, y), 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        for x, y in self.m.keys():
            if x != point[0] and y != point[1] and abs(x - point[0]) == abs(y - point[1]) and (x, point[1]) in self.m and (point[0], y) in self.m:
                res += self.m[(x, y)] * self.m[(x, point[1])] * self.m[(point[0], y)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)