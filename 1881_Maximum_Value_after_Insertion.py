class Solution:
    def maxValue(self, n: str, x: int) -> str:
        (i, neg) = (1, -1) if n[0] == '-' else (0, 1)
        while i < len(n):
            if (x * neg > int(n[i]) * neg):
                break
            i += 1
        return n[:i] + str(x) + n[i:]