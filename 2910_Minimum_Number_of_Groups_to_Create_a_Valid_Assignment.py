from typing import Counter
class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        c = Counter(balls)
        s = min(c.values())
        res = float('inf')
        for i in range(1, s+1):
            cnt = 0
            possible = True
            for v in c.values():
                a, b = v // (i+1), v % (i+1)
                if b == 0:
                    cnt += a
                elif i-b <= a:
                    cnt += a+1
                else:
                    possible = False
                    break
            if possible:
                res = min(res, cnt)
        return res