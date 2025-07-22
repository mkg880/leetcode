class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p, neg = 0, 1
        res = [0] * n
        for val in nums:
            if val > 0:
                res[p] = val
                p += 2
            else:
                res[neg] = val
                neg += 2
        return res