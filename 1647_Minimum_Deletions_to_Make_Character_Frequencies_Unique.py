class Solution:
    def minDeletions(self, s: str) -> int:
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1
        found = set()
        res = 0
        for key in m:
            freq = m[key]
            while freq > 0 and freq in found:
                freq -= 1
                res += 1
            found.add(freq)
        return res