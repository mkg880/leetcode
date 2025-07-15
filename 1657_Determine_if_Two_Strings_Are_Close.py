class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a = {}
        b = {}
        for c in word1:
            a[c] = a.get(c, 0) + 1
        for c in word2:
            b[c] = b.get(c, 0) + 1
        return a.keys() == b.keys() and sorted(list(a.values())) == sorted(list(b.values()))