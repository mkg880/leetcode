class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        m = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                val = nums[i] * nums[j]
                m[val] = m.get(val, 0) + 1
        res = 0
        for val in m:
            if m[val] > 1:
                res += comb(m[val], 2) * 8
        return res