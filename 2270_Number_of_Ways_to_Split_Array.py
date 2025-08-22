class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = 0
        r = sum(nums)
        for i in range(n-1):
            l += nums[i]
            r -= nums[i]
            if l >= r:
                res += 1
        return res