from typing import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0 if 1 not in c else c[1] - 1 if c[1] % 2 == 0 else c[1]
        for x in sorted(c.keys()):
            if x == 1:
                continue
            val = x
            cnt = 0
            while val in c and c[val] > 1:
                cnt += 1
                val **= 2
            if val not in c: cnt -= 1
            res = max(res, cnt * 2 + 1)
            x += 1
        return res