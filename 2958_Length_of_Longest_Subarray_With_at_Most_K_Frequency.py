class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n, res, m, end = len(nums), 0, {}, 0
        for start in range(n):
            while end < n:
                prev = m.get(nums[end], 0)
                if prev == k:
                    break
                m[nums[end]] = prev + 1
                end += 1
            res = max(res, end - start)
            prev = m[nums[start]]
            m[nums[start]] = prev - 1
        return res