class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        curr = float('inf')
        for i in range(n-1, -1, -1):
            suf[i] = curr
            curr = min(curr, nums[i])
        prev = nums[0]
        res = float('inf')
        for i in range(1, n-1):
            if prev < nums[i] and suf[i] < nums[i]:
                res = min(res, prev + nums[i] + suf[i])
            prev = min(prev, nums[i])
        return res if res < float('inf') else -1