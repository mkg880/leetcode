class Solution:
    def compressedString(self, word: str) -> str:
        start = 0
        res = ''
        while start < len(word):
            end = start + 1
            while end < len(word) and end - start < 9 and word[end] == word[end-1]:
                end += 1
            res += str(end - start) + word[start]
            start = end
        return res