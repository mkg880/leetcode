class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        before = 0
        after = sum(nums[1:])
        a = 0
        b = len(nums) - 1
        res = []
        for i in range(len(nums)):
            x = nums[i] * a - before
            y = after - nums[i] * b
            res.append(x + y)
            before += nums[i]
            a += 1
            if i < len(nums) - 1:
                after -= nums[i+1]
                b -= 1
        return res