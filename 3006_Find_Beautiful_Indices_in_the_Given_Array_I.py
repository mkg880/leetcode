import bisect
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        valid_j = []
        res = []
        n, x, y = len(s), len(a), len(b)
        for j in range(n-y+1):
            if s[j:j+y] == b:
                valid_j.append(j)
        for i in range(n-x+1):
            if s[i:i+x] == a:
                idx = bisect.bisect_left(valid_j, i)
                if (idx > 0 and i - valid_j[idx-1] <= k) or (idx < len(valid_j) and valid_j[idx] - i <= k):
                    res.append(i)
        return res