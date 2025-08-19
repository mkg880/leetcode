class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        m = {}
        res = 0
        mod = 10 ** 9 + 7
        for val in nums:
            rev = int(str(val)[::-1])
            d = rev - val
            cnt = m.get(d, 0)
            res = (res + cnt) % mod
            m[rev-val] = cnt + 1
        return res
