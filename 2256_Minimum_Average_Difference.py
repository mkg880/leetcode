class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = sum(nums)
        diff = float('inf')
        res = -1
        for i in range(n):
            l += nums[i]
            r -= nums[i]
            d = n - i - 1
            x = l // (i+1)
            y = r // d if d else 0
            val = abs(x-y)
            if val < diff:
                diff = val
                res = i
        return res