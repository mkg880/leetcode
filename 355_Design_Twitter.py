class Twitter:

    def __init__(self):
        self.curr = 0
        self.followers = {}
        self.heaps = {}
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        for follower in list(self.followers.get(userId, [])) + [userId]:
            if follower not in self.heaps:
                self.heaps[follower] = []
            heappush(self.heaps[follower], [self.curr, tweetId, False, userId])
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.curr, tweetId, False, userId])
        self.curr -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = self.heaps.get(userId, [])
        res = []
        temp = heap[:]
        while len(res) < 10 and heap:
            _, t, removed, _ = heappop(heap)
            if not removed:
                res.append(t)
        self.heaps[userId] = temp
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers:
            self.followers[followeeId] = set()
        if followerId not in self.followers[followeeId]:
            self.followers[followeeId].add(followerId)
            if followerId not in self.heaps:
                self.heaps[followerId] = []
            for tweet in self.tweets.get(followeeId, []):
                heappush(self.heaps[followerId], tweet)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers and followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
            for i in range(len(self.heaps[followerId])):
                if self.heaps[followerId][i][-1] == followeeId:
                    self.heaps[followerId][i][-2] = True


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)