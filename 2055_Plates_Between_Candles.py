class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        stars = 0
        prefix = [0] * len(s)
        bars = []
        for i in range(len(s)):
            if s[i] == '*':
                stars += 1
            else:
                bars.append(i)
            prefix[i] = stars
        res = []
        for l, r in queries:
            l_idx = bisect.bisect_left(bars, l)
            if l_idx == len(bars):
                res.append(0)
                continue
            left = bars[l_idx]
            right = bars[bisect.bisect_left(bars, r + 1) - 1]
            if left > r or right < l:
                res.append(0)
            else:
                res.append(prefix[right] - prefix[left])
        return res