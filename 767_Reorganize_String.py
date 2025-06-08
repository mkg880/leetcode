class Solution:
    def reorganizeString(self, s: str) -> str:
        m = {}
        for c in s:
            if c not in m:
                m[c] = 0
            m[c] += 1
        v = [[k, v] for k, v in sorted(m.items(), key=lambda item: item[1], reverse=True)]
        res = ''
        res += v[0][0]
        if v[0][1] > 0:
            v[0][1] -= 1
        for i in range(1, len(s)):
            v = sorted(v, key=lambda item: item[1], reverse=True)
            if res[i-1] != v[0][0]:
                res += v[0][0]
                v[0][1] -= 1
            elif len(v) == 1 or v[1][1] <= 0:
                return ''
            else:
                res += v[1][0]
                v[1][1] -= 1
        return res