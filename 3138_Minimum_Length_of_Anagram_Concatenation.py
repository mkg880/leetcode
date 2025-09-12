from typing import Counter
class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for k in range(1, n+1):
            if n % k != 0:
                continue
            c = Counter(s[:k])
            valid = True
            for i in range(k, n, k):
                if c != Counter(s[i:i+k]):
                    valid = False
                    break
            if valid:
                return k