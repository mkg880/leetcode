class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = [ceil(d / s) for d, s in zip(dist, speed)]
        times.sort()
        t = 0
        while t < len(times) and times[t] > t:
            t += 1
        return t