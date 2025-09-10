from math import ceil
class Solution:
    def minOperations(self, k: int) -> int:
        res = float('inf')
        for inc in range(k):
            res = min(res, inc + ceil(k / (inc+1)) - 1)
        return res