class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = {}
        n = len(target)
        res = 0
        for s in nums:
            m = len(s)
            if m >= n:
                continue
            if target[:m] == s:
                res += cnt.get(target[m:], 0)
            if target[-m:] == s:
                res += cnt.get(target[:-m], 0)
            cnt[s] = cnt.get(s, 0) + 1
        return res