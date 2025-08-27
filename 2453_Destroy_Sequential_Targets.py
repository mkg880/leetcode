from typing import Counter
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        c = Counter([x % space for x in nums])
        val = max(c.values())
        res = float('inf')
        for x in nums:
            if c[x%space] == val and x < res:
                res = x
        return res