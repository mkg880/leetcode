class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        interval = [startTime, endTime-1]
        idx = bisect_left(self.intervals, interval)
        if (idx-1 >= 0 and self.intervals[idx-1][1] >= startTime) or (idx < len(self.intervals) and self.intervals[idx][0] <= endTime-1):
            return False
        self.intervals.insert(idx, interval)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)