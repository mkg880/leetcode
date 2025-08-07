class MagicDictionary:

    def __init__(self):
        self.m = {}

    def _insert(self, word: str) -> None:
        m = self.m
        for c in word + '/':
            if c in m:
                m = m[c]
            else:
                m[c] = {}
                m = m[c]

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self._insert(word)

    def search(self, searchWord: str) -> bool:
        stack = [(self.m, 0, False)]
        while stack:
            m, i, changed = stack.pop()
            if i == len(searchWord):
                if changed and '/' in m:
                    return True
                continue
            c = searchWord[i]
            if changed:
                if c in m:
                    stack.append((m[c], i+1, True))
                continue
            for key in m:
                stack.append((m[key], i+1, key!=c))
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)