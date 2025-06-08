class Solution:

    def __init__(self, w: List[int]):
        self.limits = []
        prev = 0
        total = sum(w)
        for val in w:
            prev += (val / total) * 100
            self.limits.append(prev)

    def pickIndex(self) -> int:
        r = random.randint(1, 100)
        low = 0
        hi = len(self.limits) - 1
        while low < hi:
            mid = (low + hi) // 2
            if self.limits[mid] < r:
                low = mid + 1
            else:
                hi = mid
        return hi



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()