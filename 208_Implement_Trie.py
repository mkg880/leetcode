class Trie:

    def __init__(self):
        self.m = {}

    def insert(self, word: str) -> None:
        m = self.m
        for c in word + '/':
            if c in m:
                m = m[c]
            else:
                m[c] = {}
                m = m[c]

    def search(self, word: str) -> bool:
        m = self.m
        for c in word + '/':
            if c not in m:
                return False
            m = m[c]
        return True

    def startsWith(self, prefix: str) -> bool:
        m = self.m
        for c in prefix:
            if c not in m:
                return False
            m = m[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)