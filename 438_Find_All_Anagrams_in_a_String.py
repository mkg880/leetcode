class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        target = {}
        for c in p:
            target[c] = target.get(c, 0) + 1
        actual = {}
        n = len(p)
        end = n
        for i in range(end):
            actual[s[i]] = actual.get(s[i], 0) + 1
        res = []
        while end <= len(s):
            start = end - n
            if actual == target:
                res.append(start)
            actual[s[start]] -= 1
            if actual[s[start]] == 0:
                del actual[s[start]]
            if end < len(s):
                actual[s[end]] = actual.get(s[end], 0) + 1
            end += 1
        return res