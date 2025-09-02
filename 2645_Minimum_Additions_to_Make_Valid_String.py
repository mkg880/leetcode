class Solution:
    def addMinimum(self, word: str) -> int:
        s = 'abc'
        i, j = 0, 0
        res = 0
        while i < len(word):
            if word[i] != s[j]:
                res += 1
            else:
                i += 1
            j = (j+1) % 3
        return res + ((3-j) % 3)