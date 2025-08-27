class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        l = 1
        res = 1
        prev = ord(s[0])
        for i in range(1, len(s)):
            if ord(s[i]) == prev + 1:
                l += 1
                res = max(res, l)
            else:
                l = 1
            prev = ord(s[i])
        return res