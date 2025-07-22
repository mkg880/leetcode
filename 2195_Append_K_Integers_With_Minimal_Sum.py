class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = 1
        res = 0
        for val in nums:
            if curr < val:
                n = min(val - curr, k)
                res += n * (n+1) // 2 + (n * (curr - 1))
                k -= n
            if k == 0:
                return res
            curr = val + 1
        if k:
            res += k * (k+1) // 2 + (k * (curr - 1))
        return res