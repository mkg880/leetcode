class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.m = {}
        self.t = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.m[tokenId] = currentTime + self.t

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.m.get(tokenId, -1) > currentTime:
            self.m[tokenId]  = currentTime + self.t

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return len([x for x in self.m.values() if x > currentTime])


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)