class UndergroundSystem:

    def __init__(self):
        self.m = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.m[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.m[id]
        self.times[(startStation, stationName)] = self.times.get((startStation, stationName), []) + [t-startTime]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.times[(startStation, endStation)]) / len(self.times[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)