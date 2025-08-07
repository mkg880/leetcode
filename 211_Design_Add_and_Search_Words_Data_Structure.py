class WordDictionary:

    def __init__(self):
        self.m = {}

    def addWord(self, word: str) -> None:
        m = self.m
        for c in word + '/':
            if c in m:
                m = m[c]
            else:
                m[c] = {}
                m = m[c]

    def search(self, word: str) -> bool:
        word += '/'
        stack = [(self.m, 0)]
        while stack:
            m, i = stack.pop()
            if i == len(word):
                return True
            if word[i] == '.':
                for key in m:
                    if key == '/':
                        continue
                    stack.append((m[key], i+1))
            elif word[i] in m:
                stack.append((m[word[i]], i+1))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)