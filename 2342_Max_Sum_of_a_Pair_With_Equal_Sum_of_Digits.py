class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        m = {}
        res = -1
        for num in nums:
            s = str(num)
            val = 0
            for c in s:
                val += int(c)
            if val in m:
                res = max(res, m[val] + num)
                m[val] = max(m[val], num)
            else:
                m[val] = num
        return res