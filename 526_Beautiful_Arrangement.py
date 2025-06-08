class Solution:
    def recurse(self, nums, i, n):
        if i == n+1:
            return 1
        total = 0
        for j in range(len(nums)):
            if nums[j] % i == 0 or i % nums[j] == 0:
                total += self.recurse(nums[:j] + nums[j+1:], i+1, n)
        return total
    def countArrangement(self, n: int) -> int:
        dp = [i for i in range(1, n+1)]
        return self.recurse(dp, 1, n)