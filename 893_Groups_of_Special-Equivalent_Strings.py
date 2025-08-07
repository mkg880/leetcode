class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        m = set()
        for word in words:
            even = [0] * 26
            odd = [0] * 26
            for i in range(len(word)):
                if i % 2 == 0:
                    even[ord(word[i]) - ord('a')] += 1
                else:
                    odd[ord(word[i]) - ord('a')] += 1
            key = (tuple(even), tuple(odd))
            m.add(key)
        return len(m)