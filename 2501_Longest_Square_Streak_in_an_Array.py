class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        m = {}
        res = -1
        for val in nums:
            if val in m:
                m[val ** 2] = m[val] + 1
                res = max(res, m[val] + 1)
            else:
                m[val ** 2] = 1
        return res