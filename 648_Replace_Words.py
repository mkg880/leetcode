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
        cnt = 0
        for c in word + '/':
            if '/' in m:
                return word[:cnt]
            if c not in m:
                return False
            cnt += 1
            m = m[c]
        return word


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie()
        for root in dictionary:
            t.insert(root)
        res = []
        for word in sentence.split():
            pre = t.search(word)
            if pre == False:
                pre = word
            res.append(pre)
        return ' '.join(res)

        