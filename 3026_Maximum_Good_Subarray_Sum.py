class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = float('-inf')
        m = {}
        pre = [0]
        for i in range(n):
            pre.append(pre[-1] + nums[i])
            if nums[i] + k in m:
                res = max(res, pre[-1] - pre[m[nums[i] + k]])
            if nums[i] - k in m:
                res = max(res, pre[-1] - pre[m[nums[i] - k]])
            if nums[i] not in m or pre[i] <= pre[m[nums[i]]]:
                m[nums[i]] = i
        return res if res > float('-inf') else 0