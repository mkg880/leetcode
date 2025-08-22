import bisect
from math import ceil
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for spell in spells:
            t = ceil(success / spell)
            idx = bisect.bisect_left(potions, t)
            res.append(len(potions) - idx)
        return res