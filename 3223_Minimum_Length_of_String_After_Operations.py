class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = {}
        for c in s:
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1
        res = 0
        for key in cnt:
            if cnt[key] % 2 == 0:
                res += 2
            else:
                res += 1
        return res