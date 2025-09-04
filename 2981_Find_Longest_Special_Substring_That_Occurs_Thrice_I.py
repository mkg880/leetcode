class Solution:
    def maximumLength(self, s: str) -> int:
        m = {}
        n = len(s)
        res = -1
        for start in range(n):
            curr = ''
            for end in range(start, n):
                if s[end] != s[start]:
                    break
                curr += s[end]
                m[curr] = m.get(curr, 0) + 1
                if m[curr] >= 3:
                    res = max(res, len(curr))
                end += 1
        return res