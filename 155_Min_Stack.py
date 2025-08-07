class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minval = val
        elif val > self.minval:
            self.stack.append(val)
        else:
            encoded = 2 * val - self.minval
            self.stack.append(encoded)
            self.minval = val

    def pop(self) -> None:
        top = self.stack.pop()
        if top < self.minval:
            self.minval = 2 * self.minval - top

    def top(self) -> int:
        top = self.stack[-1]
        return max(self.minval, top)

    def getMin(self) -> int:
        return self.minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()