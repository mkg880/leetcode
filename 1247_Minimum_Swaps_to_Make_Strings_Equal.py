class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x, y = 0, 0
        swaps = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    if x:
                        x -= 1
                        swaps += 1
                    else:
                        x += 1
                else:
                    if y:
                        y -= 1
                        swaps += 1
                    else:
                        y += 1
        if x + y == 1:
            return -1
        if x + y == 0:
            return swaps
        return swaps + 2