class Trie:

    def __init__(self):
        self.m = {}
        self.dup = set()

    def insert(self, word: str) -> None:
        m = self.m
        for c in word[::-1] + '/':
            if c in m:
                if c == '/':
                    self.dup.add(word)
                m = m[c]
            else:
                m[c] = {}
                m = m[c]

    def endsWith(self, prefix: str) -> bool:
        m = self.m
        for c in prefix[::-1]:
            if c not in m:
                return False
            m = m[c]
        return len(m) > 1
    
    def isDup(self, word: str) -> bool:
        return word in self.dup

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        t = Trie()
        res = 0
        for word in words:
            t.insert(word)
            res += len(word) + 1
        dups_found = set()
        for word in words:
            if (t.isDup(word) and word in dups_found) or t.endsWith(word):
                res -= len(word) + 1
            elif t.isDup(word):
                dups_found.add(word)
        return res