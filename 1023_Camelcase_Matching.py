class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for word in queries:
            i, j = 0, 0
            b = True
            while i < len(word) and j < len(pattern):
                if word[i] == pattern[j]:
                    i += 1
                    j += 1
                elif 'A' <= word[i] <= 'Z':
                    b = False
                    break
                else:
                    i += 1
            b = b and j == len(pattern) and all(['a' <= c <= 'z' for c in word[i:]])
            res.append(b)
        return res