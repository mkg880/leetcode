class Solution:
    def makeFancyString(self, s: str) -> str:
        arr = []
        res = ''
        c = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == c:
                cnt += 1
            else:
                res += c * min(2, cnt)
                c = s[i]
                cnt = 1
        res += c * min(2, cnt)
        return res