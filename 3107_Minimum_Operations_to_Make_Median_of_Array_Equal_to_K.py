class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mid = n // 2
        res = 0
        for i in range(n):
            if (i <= mid and nums[i] > k) or (i >= mid and nums[i] < k):
                res += abs(k - nums[i])
        return res