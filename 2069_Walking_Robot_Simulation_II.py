class Robot:

    def __init__(self, width: int, height: int):
        self.w = width - 1
        self.h = height - 1
        self.pos = 0
        self.perim = 2 * self.w + 2 * self.h
        self.started = False

    def step(self, num: int) -> None:
        self.pos += num
        self.pos %= self.perim
        self.started = True


    def getPos(self) -> List[int]:
        threshold = self.w
        cnt = 0
        loc = self.pos
        while loc > threshold:
            loc -= threshold
            threshold = self.h if threshold == self.w else self.w
            cnt += 1
        if cnt == 0:
            return [loc, 0]
        if cnt == 1:
            return [self.w, loc]
        if cnt == 2:
            return [self.w - loc, self.h]
        return [0, self.h - loc]


    def getDir(self) -> str:
        pos = ["East", "North", "West", "South"]
        cnt = 0
        loc = self.pos
        if not loc and self.started:
            return "South"
        threshold = self.w
        while loc > threshold:
            loc -= threshold
            threshold = self.h if threshold == self.w else self.w
            cnt += 1
        return pos[cnt]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()