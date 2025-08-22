from typing import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        m = Counter(tasks)
        res = 0
        for val in m.values():
            if val == 1:
                return -1
            if val >= 3:
                res += val // 3
                val %= 3
            if val == 1:
                val = 4
                res -= 1
            if val >= 2:
                res += val // 2
        return res