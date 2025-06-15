class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if len(s) == 1:
            return m[s]
        i = 0
        res = 0
        while i < len(s) - 1:
            if m[s[i]] < m[s[i+1]]:
                res += m[s[i+1]] - m[s[i]]
                i += 1
            else:
                res += m[s[i]]
            i += 1
        if m[s[-2]] >= m[s[-1]]:
            res += m[s[-1]]
        return res