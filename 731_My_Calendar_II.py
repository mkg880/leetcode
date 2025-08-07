class MyCalendarTwo:

    def __init__(self):
        self.single = []
        self.double = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.double:
            if max(s, startTime) < min(e, endTime):
                return False
        for s, e in self.single:
            max_s = max(s, startTime)
            min_e = min(e, endTime)
            if max_s < min_e:
                self.double.append((max_s, min_e))
        self.single.append((startTime, endTime))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)