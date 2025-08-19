class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        def diff(a, b):
            d = ord(a) - ord(b)
            return d if d >= 0 else d + 26
        options = {i: k // 26 for i in range(27)}
        for i in range(k % 26 + 1):
            options[i] += 1
        for i in range(len(s)):
            d = diff(t[i], s[i])
            if d > 0 and options[d] == 0:
                return False
            options[d] -= 1
        return True