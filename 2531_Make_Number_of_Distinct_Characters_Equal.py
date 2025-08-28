from typing import Counter
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        m, n = len(c1), len(c2)
        if abs(m - n) > 2:
            return False
        for key1 in c1:
            for key2 in c2:
                diff1 = -1 if c1[key1] == 1 and key1 != key2 else 0
                if key2 not in c1:
                    diff1 += 1
                diff2 = -1 if c2[key2] == 1 and key1 != key2 else 0
                if key1 not in c2:
                    diff2 += 1
                if m + diff1 == n + diff2:
                    return True
        return False