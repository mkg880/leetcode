class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        for pens in range(total // cost1 + 1):
            rem = total - cost1 * pens
            res += rem // cost2 + 1
        return res