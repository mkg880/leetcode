class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}
        for i, c in enumerate(word):
            if c.isupper():
                l = c.lower()
                if l not in upper:
                    upper[l] = i
            else:
                lower[c] = i
        res = 0
        for key in lower:
            if key in upper and lower[key] < upper[key]:
                res += 1
        return res