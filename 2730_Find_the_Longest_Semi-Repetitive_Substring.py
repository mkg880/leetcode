class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        pairs = []
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                pairs.append(i)
        if len(pairs) < 2:
            return len(s)
        res = 0
        for i in range(len(pairs)):
            l = -1 if i == 0 else pairs[i-1]
            r = len(s) - 1 if i == len(pairs) - 1 else pairs[i+1]
            res = max(res, r-l)
        return res