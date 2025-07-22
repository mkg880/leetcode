class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        idx, i, j = 0, 0, 0
        m, n = len(s), len(spaces)
        total = m + n
        res = ''
        while len(res) < total:
            nextSpace = spaces[j] if j < n else -1
            if i == nextSpace:
                res += ' '
                j += 1
            else:
                res += s[i]
                i += 1
        return res