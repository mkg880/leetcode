class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        m = {}
        res = 0
        def rec(i):
            nonlocal res
            if i == len(nums):
                res += 1
                return
            rec(i+1)
            if not m.get(nums[i] - k, 0) > 0:
                m[nums[i]] = m.get(nums[i], 0) + 1
                rec(i+1)
                m[nums[i]] -= 1
        nums.sort()
        rec(0)
        return res - 1