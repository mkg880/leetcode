class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pre = [0] * (len(nums) + 1)
        last = {}
        res = 0
        start = 0
        for i, val in enumerate(nums):
            if val in last and last[val] >= start:
                start = last[val] + 1
            curr = pre[i] - pre[start] + val
            res = max(res, curr)
            pre[i+1] = pre[i] + val
            last[val] = i
        return res