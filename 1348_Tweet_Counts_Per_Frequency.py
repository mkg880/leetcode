import bisect
class TweetCounts:

    def __init__(self):
        self.m = {}
        self.step = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        arr = self.m.get(tweetName, [])
        bisect.insort(arr, time)
        self.m[tweetName] = arr

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.m:
            return []
        arr = self.m[tweetName]
        step = self.step[freq]
        res = []
        i = bisect.bisect_left(arr, startTime)
        start = startTime
        while start <= endTime:
            end = min(start + step - 1, endTime)
            prev = i
            while i < len(arr) and arr[i] <= end:
                i += 1
            res.append(i-prev)
            start = end + 1
        return res



# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)