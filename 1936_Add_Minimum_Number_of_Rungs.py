class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = 0
        for i in range(len(rungs)):
            prev = rungs[i-1] if i > 0 else 0
            res += ceil((rungs[i] - prev) / dist) - 1
        return res