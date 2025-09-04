class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels = set('aeiou')
        res = 0
        for start in range(n):
            v, c = 0, 0
            for end in range(start, n):
                if s[end] in vowels: v += 1
                else: c += 1
                if v == c and (v * c) % k == 0:
                    res += 1
        return res