class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        sort = sorted(nums)
        d = {}
        sum = 0
        for i in range(len(nums)):
            sum += sort[i]
            d[i] = sum
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum == d[i]:
                return i + 1
        return -1