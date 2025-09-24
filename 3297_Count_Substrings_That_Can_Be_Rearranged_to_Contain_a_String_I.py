from typing import Counter
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        c2 = Counter(word2)
        c1 = {}
        end = 0
        n = len(word1)
        res = 0
        invalid = set(c2.keys())
        for start in range(n):
            while end < n and invalid:
                c1[word1[end]] = c1.get(word1[end], 0) + 1
                if word1[end] in invalid and c1[word1[end]] >= c2[word1[end]]:
                    invalid.remove(word1[end])
                end += 1
            res += n - end + 1 if not invalid else 0
            c1[word1[start]] -= 1
            if word1[start] in c2 and c1[word1[start]] < c2[word1[start]]:
                invalid.add(word1[start])
        return res