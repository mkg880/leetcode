class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cnt = [0] * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            val = 1 if nums[i-1] % modulo == k else 0
            cnt[i] = cnt[i-1] + val
        m = {}
        res = 0
        for i in range(len(nums)+1):
            res += m.get((cnt[i] + modulo - k) % modulo, 0)
            m[cnt[i] % modulo] = m.get(cnt[i] % modulo, 0) + 1
        return res