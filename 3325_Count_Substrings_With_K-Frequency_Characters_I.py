class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        m = {}
        end = 0
        res = 0
        for start in range(n):
            ma = max(m.values()) if m else 0
            while end < n and ma < k:
                m[s[end]] = m.get(s[end], 0) + 1
                ma = max(ma, m[s[end]])
                end += 1
            if ma == k:
                res += n - end + 1
            else:
                break
            m[s[start]] -= 1
        return res