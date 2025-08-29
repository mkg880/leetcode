import bisect
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        pre = [0] * (n+1)
        curr = 0
        for i in range(n+1):
            pre[i] = curr
            if i < n: curr += nums[i]
        res = []
        for q in queries:
            l, r = bisect.bisect_left(nums, q), bisect.bisect_right(nums, q)
            res.append(q * (l+r-n) - pre[l] + pre[n] - pre[r])
        return res