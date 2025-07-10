class Solution:
    def minInsertions(self, s: str) -> int:
        cnt = 0
        res = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                cnt += 1
            else:
                if cnt == 0:
                    res += 1
                else:
                    cnt -= 1
                if i + 1 == len(s) or s[i+1] == '(':
                    res += 1
                else:
                    i += 1
            i += 1
        res += cnt * 2
        return res