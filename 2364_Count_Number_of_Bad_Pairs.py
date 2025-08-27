class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        cnt = 0
        m = {}
        n = len(nums)
        for i in range(n):
            diff = i - nums[i]
            prev = m.get(diff, 0)
            cnt += prev
            m[diff] = prev + 1
        return n * (n-1) // 2 - cnt