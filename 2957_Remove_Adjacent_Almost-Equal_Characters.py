class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n, i, res = len(word), 1, 0
        while i < n:
            if abs(ord(word[i]) - ord(word[i-1])) <= 1:
                res += 1
                i += 1
            i += 1
        return res