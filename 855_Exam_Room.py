class ExamRoom:

    def __init__(self, n: int):
        self.seats = []
        self.n = n

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        max_val = self.seats[0]
        res = 0
        for i in range(1, len(self.seats)):
            d = (self.seats[i] - self.seats[i-1]) // 2
            seat = self.seats[i-1] + d
            if d > max_val:
                max_val = d
                res = seat
        d = self.n - 1 - self.seats[-1]
        if d > max_val:
            res = self.n - 1
        bisect.insort(self.seats, res)
        return res
    
    def leave(self, p: int) -> None:
        self.seats.pop(bisect.bisect_left(self.seats, p))


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)