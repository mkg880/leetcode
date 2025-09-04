from typing import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        mul, cnt, total = 1, 0, 0
        for val in sorted(list(c.values()), reverse=True):
            total += val * mul
            cnt += 1
            if cnt == 8:
                mul += 1
                cnt = 0
        return total