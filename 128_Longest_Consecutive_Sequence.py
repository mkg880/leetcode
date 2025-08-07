class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        res = 1
        for val in nums:
            inc, dec = 1, 1
            if val - 1 in m:
                inc += m[val-1][0]
            if val + 1 in m:
                dec += m[val+1][1]
            res = max(res, inc + dec - 1)
            m[val] = [inc, dec]
        return res