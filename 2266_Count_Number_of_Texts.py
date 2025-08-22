from itertools import groupby
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10 ** 9 + 7
        groups = []
        max_three = 0
        max_four = 0
        for key, group in groupby(pressedKeys):
            x, p = len(list(group)), 4 if key == '7' or key == '9' else 3
            if p == 3:
                max_three = max(max_three, x+1)
            else:
                max_four = max(max_four, x+1)
            groups.append((x, p))
        cnt_three = [0] * max_three
        cnt_four = [0] * max_four
        for i in range(max_three):
            if i < 2:
                cnt_three[i] = 1
                continue
            for k in range(1, 4):
                if i-k < 0:
                    continue
                cnt_three[i] += cnt_three[i-k]
                cnt_three[i] %= mod
        for i in range(max_four):
            if i < 2:
                cnt_four[i] = 1
                continue
            for k in range(1, 5):
                if i-k < 0:
                    continue
                cnt_four[i] += cnt_four[i-k]
                cnt_four[i] %= mod
        res = 1
        for x, p in groups:
            val = cnt_three[x] if p == 3 else cnt_four[x]
            res *= val
            res %= mod
        return res