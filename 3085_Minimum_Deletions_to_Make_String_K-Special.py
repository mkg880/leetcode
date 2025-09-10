class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        m = {}
        for c in word:
            m[c] = m.get(c, 0) + 1
        arr = sorted([m[key] for key in m])
        before = 0
        r = 0
        res = float('inf')
        while r < len(arr) and arr[r] - arr[0] <= k:
            r += 1
        rem = 0
        for i in range(r, len(arr)):
            rem += arr[i] - (arr[0] + k)
        for i in range(len(arr)):
            while r < len(arr) and arr[r] - arr[i] <= k:
                rem -= arr[r] - (arr[i-1] + k)
                r += 1
            if i > 0:
                rem -= (len(arr) - r) * (arr[i] - arr[i-1])
            res = min(res, rem + before)
            before += arr[i]
        return res