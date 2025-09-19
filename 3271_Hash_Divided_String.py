class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        tot = 0
        res = ''
        for i in range(n):
            if i > 0 and i % k == 0:
                res += chr(tot + ord('a'))
                tot = 0
            val = ord(s[i]) - ord('a')
            tot = (tot + val) % 26
        return res + chr(tot + ord('a'))