class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        res = ""
        while i < m and j < n:
            x, y = word1[i:], word2[j:]
            if x > y:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
        if i < m:
            res += word1[i:]
        if j < n:
            res += word2[j:]
        return res