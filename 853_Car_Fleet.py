class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        max_time = 0
        res = 0
        arr = sorted(list(zip(position, speed)))
        for p, s in reversed(arr):
            t = (target - p) / s
            if t > max_time:
                res += 1
                max_time = t
        return res