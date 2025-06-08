class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def cmp(a, b):
            if len(a) != len(b):
                return len(b) - len(a)
            if a < b:
                return -1
            return 1
        dictionary.sort(key=cmp_to_key(cmp))
        for word in dictionary:
            i, j = 0, 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            if i == len(word):
                return word
        return ""