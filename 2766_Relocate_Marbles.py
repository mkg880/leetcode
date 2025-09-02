from typing import Counter
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        m = Counter(nums)
        for f, t in zip(moveFrom, moveTo):
            if f != t and f in m:
                m[t] = m.get(t, 0) + m[f]
                del m[f]
        return sorted(list(m.keys()))