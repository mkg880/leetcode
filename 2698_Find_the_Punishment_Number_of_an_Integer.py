class Solution:
    def punishmentNumber(self, n: int) -> int:
        def possible(s, target):
            if not s and not target:
                return True
            if target < 0:
                return False
            l = 0
            for i in range(len(s)):
                l = l * 10 + int(s[i])
                if possible(s[i+1:], target - l):
                    return True
            return False
        res = 0
        for i in range(1, n+1):
            sq = i * i
            if possible(str(sq), i):
                res += sq
        return res