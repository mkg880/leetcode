class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        post = [0] * n
        curr = 0
        for i in range(n):
            pre[i] = curr
            curr = max(curr, nums[i])
        curr = float('inf')
        for i in range(n-1, -1, -1):
            post[i] = curr
            curr = min(curr, nums[i])
        res = 0
        for i in range(1, n - 1):
            if pre[i] < nums[i] < post[i]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
        return res