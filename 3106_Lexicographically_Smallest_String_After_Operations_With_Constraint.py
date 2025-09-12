class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def dist(a, b):
            x, y = ord(a) - ord('a'), ord(b) - ord('a')
            mi, ma = min(x, y), max(x, y)
            return min(ma - mi, mi - ma + 26)
        tot = 0
        n = len(s)
        res = ''
        for i in range(n):
            for j in range(26):
                c = chr(ord('a') + j)
                d = dist(c, s[i])
                if d + tot <= k:
                    res += c
                    tot += d
                    break
        return res