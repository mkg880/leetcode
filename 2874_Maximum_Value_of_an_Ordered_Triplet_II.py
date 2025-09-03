class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        curr = 0
        for i in range(n-1, -1, -1):
            suf[i] = curr
            curr = max(curr, nums[i])
        res = 0
        prev = nums[0]
        for i in range(1, n-1):
            res = max(res, (prev - nums[i]) * suf[i])
            prev = max(prev, nums[i])
        return res