class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        start = 0
        res = 0
        curr = 0
        for i in range(len(s)):
            if s[i] not in m or m[s[i]] < start:
                curr += 1
                res = max(res, curr)
            else:
                start = m[s[i]] + 1
                curr = i - m[s[i]]
            m[s[i]] = i
        return res