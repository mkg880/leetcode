from typing import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        c = Counter(s)
        if min(c.get('a', 0), c.get('b', 0), c.get('c', 0)) < k:
            return -1
        for key in ['a', 'b', 'c']:
            c[key] = c.get(key, 0) - k
        m = {'a': 0, 'b': 0, 'c': 0}
        m[s[0]] = 1
        end = 0
        n = len(s)
        while end < n and all(m[key] <= c[key] for key in m):
            end += 1
            m[s[end]] += 1
        res = n - end
        for start in range(1, n):
            m[s[start-1]] -= 1
            while end < n and all(m[key] <= c[key] for key in m):
                end += 1
                if end < n:
                    m[s[end]] += 1
            res = min(res, n - end + start)
        return res