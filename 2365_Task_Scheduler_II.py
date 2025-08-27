class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        m = {}
        t = 0
        for val in tasks:
            comp = max(m[val] + space + 1, t) if val in m else t
            m[val] = comp
            t = comp + 1
        return t