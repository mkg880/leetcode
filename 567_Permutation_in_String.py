class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        d2 = {}
        for c in s1:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1
        i = 0
        start = 0
        while i < len(s2):
            c = s2[i]
            if c in d1:
                if c in d2 and d2[c] >= d1[c]:
                    start += 1
                    i = start
                    d2 = {}
                else:
                    if c in d2:
                        d2[c] += 1
                    else:
                        d2[c] = 1
                    if i - start + 1 == len(s1) and d1 == d2:
                        return True
                    i += 1
            else:
                start += 1
                i = start
                d2 = {}
        return False