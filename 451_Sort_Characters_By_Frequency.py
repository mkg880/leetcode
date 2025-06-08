class Solution:
    def frequencySort(self, s: str) -> str:
        m = {}
        for c in s:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        sort = {k: v for k, v in sorted(m.items(), key=lambda item: -item[1])}
        res = ''
        for c in sort:
            res += c * sort[c]
        return res