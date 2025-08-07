class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        total = 0
        res = float('inf')
        for i in range(n + 1):
            pre[i] = total
            if i < n:
                total += nums[i]
        for i in range(n+1):
            val = pre[i] - target
            if val < 0:
                continue
            idx = bisect_left(pre, val)
            if pre[idx] > val:
                idx -= 1
            res = min(res, i - idx)
        return res if res < float('inf') else 0

