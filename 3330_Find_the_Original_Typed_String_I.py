class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        curr = word[0]
        size = 0
        for i in range(len(word)):
            if word[i] == curr:
                size += 1
            else:
                res += size - 1
                size = 1
                curr = word[i]
        return res + size - 1