class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        m = {}
        m[s[0]] = 1
        while end < len(s) and (len(m) < 2 or sum(m.values()) - max(m.values()) <= k):
            end += 1
            if end < len(s):
                m[s[end]] = m.get(s[end], 0) + 1
        res = end
        while start < len(s) and end < len(s):
            m[s[start]] -= 1
            if m[s[start]] == 0:
                del m[s[start]]
            start += 1
            while end < len(s) and (len(m) < 2 or sum(m.values()) - max(m.values()) <= k):
                end += 1
                if end < len(s):
                    m[s[end]] = m.get(s[end], 0) + 1
            res = max(res, end - start)
        return res