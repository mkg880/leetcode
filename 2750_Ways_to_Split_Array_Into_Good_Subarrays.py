class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        ones = [i for i in range(len(nums)) if nums[i]]
        res = 1
        mod = 10 ** 9 + 7
        if len(ones) < 2:
            return len(ones)
        for i in range(1, len(ones)):
            res = (res * (ones[i] - ones[i-1])) % mod
        return res