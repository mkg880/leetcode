class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        z = s.count('0')
        o = n - z
        if (n % 2 == 0 and o != z) or (abs(z-o) > 1):
            return -1
        valid = ''.join(['1' if i % 2 == 0 else '0' for i in range(n)])
        swaps = 0
        for i in range(n):
            if valid[i] != s[i]:
                swaps += 1
        swaps2 = n - swaps
        swaps, swaps2 = swaps // 2, swaps2 // 2
        if z == o:
            return min(swaps, swaps2)
        elif o > z:
            return swaps
        else:
            return swaps2 