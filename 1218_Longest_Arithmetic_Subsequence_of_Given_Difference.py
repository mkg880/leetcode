class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        m = {}
        res = 0
        for val in arr:
            d = val - difference
            m[val] = m.get(d, 0) + 1
            res = max(res, m[val])
        return res