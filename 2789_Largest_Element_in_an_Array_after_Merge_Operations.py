class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        curr = n-2
        while curr >= 0 and nums[curr] > nums[curr+1]:
            curr -= 1
        res = max(nums)
        while curr >= 0:
            nex = nums[curr+1]
            while curr >= 0 and nums[curr] <= nex:
                nex += nums[curr]
                curr -= 1
            res = max(res, nex)
            curr -= 1
        return res