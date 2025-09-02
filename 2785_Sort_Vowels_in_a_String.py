from typing import Counter
class Solution:
    def sortVowels(self, s: str) -> str:
        v = 'AEIOUaeiou'
        v_set = set(v)
        c = Counter(s)
        i = 0
        res = ''
        for ch in s:
            if ch not in v_set:
                res += ch
            else:
                while c[v[i]] == 0:
                    i += 1
                res += v[i]
                c[v[i]] -= 1
        return res