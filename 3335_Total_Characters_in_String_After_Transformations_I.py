from typing import Counter
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        c = Counter(s)
        for _ in range(t):
            m = {}
            for key in c:
                if key == 'z':
                    m['a'] = m.get('a', 0) + c[key]
                    m['b'] = m.get('b', 0) + c[key]
                else:
                    ch = chr(ord(key) + 1)
                    m[ch] = m.get(ch, 0) + c[key]
            c = m
        return sum(c.values()) % (10 ** 9 + 7)