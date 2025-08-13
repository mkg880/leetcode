class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c = 0, 0, 0
        j = 0
        res = 0
        n = len(s)
        for i in range(n):
            while j < n and (not a or not b or not c):
                if s[j] == 'a':
                    a += 1
                elif s[j] == 'b':
                    b += 1
                else:
                    c += 1
                j += 1
            if a and b and c:
                res += n - j + 1
                if s[i] == 'a':
                    a -= 1
                elif s[i] == 'b':
                    b -= 1
                else:
                    c -= 1
            else:
                return res
        return res
