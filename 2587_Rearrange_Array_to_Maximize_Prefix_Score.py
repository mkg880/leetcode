class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre <= 0:
                return i
        return len(nums)