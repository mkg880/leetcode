class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            if len(word) != len(pattern):
                continue
            m = {}
            valid = True
            for c1, c2 in zip(word, pattern):
                if (c1 in m and m[c1] != c2) or (c1 not in m and c2 in set(m.values())):
                    valid = False
                    break
                m[c1] = c2
            if valid:
                res.append(word)
        return res