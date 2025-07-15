class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        m = {}
        res = 0
        for val in nums:
            if k - val in m:
                res += 1
                m[k-val] -= 1
                if m[k-val] == 0:
                    del m[k-val]
            else:
                m[val] = m.get(val, 0) + 1
        return res