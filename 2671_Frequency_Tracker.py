class FrequencyTracker:

    def __init__(self):
        self.a = {}
        self.b = {}

    def add(self, number: int) -> None:
        prev = self.a.get(number, 0)
        if prev:
            self.b[prev] -= 1
        self.b[prev+1] = self.b.get(prev+1, 0) + 1
        self.a[number] = prev+1

    def deleteOne(self, number: int) -> None:
        if number not in self.a or not self.a[number]:
            return
        prev = self.a[number]
        self.b[prev] -= 1
        self.b[prev-1] = self.b.get(prev-1, 0) + 1
        self.a[number] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.b.get(frequency, 0) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)