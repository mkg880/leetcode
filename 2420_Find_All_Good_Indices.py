class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 0:
            return list(range(n))
        if n == 1:
            return []
        pre = [0] * n
        pre[1] = 1
        for i in range(2, n):
            if nums[i-1] > nums[i-2]:
                pre[i] = 1
            else:
                pre[i] = pre[i-1] + 1
        post = [0] * n
        post[-2] = 1
        for i in range(n-3, -1, -1):
            if nums[i+1] > nums[i+2]:
                post[i] = 1
            else:
                post[i] = post[i+1] + 1
        return [i for i in range(n) if pre[i] >= k and post[i] >= k]