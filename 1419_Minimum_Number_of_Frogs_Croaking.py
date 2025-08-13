class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt = [0] * 5
        idx = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        curr = 0
        res = 0
        for c in croakOfFrogs:
            n = idx[c]
            cnt[n] += 1
            if n == 0:
                curr += 1
                res = max(res, curr)
                continue
            cnt[n-1] -= 1
            if cnt[n-1] < 0:
                return -1
            elif n == 4:
                curr -= 1
        return res if curr == 0 else -1