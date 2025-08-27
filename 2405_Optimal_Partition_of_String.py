class Solution:
    def partitionString(self, s: str) -> int:
        m = {}
        start = 0
        res = 1
        for i in range(len(s)):
            if s[i] in m and m[s[i]] >= start:
                res += 1
                start = i
            m[s[i]] = i
        return res