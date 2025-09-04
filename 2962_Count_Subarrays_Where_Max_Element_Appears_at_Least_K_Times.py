class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n, max_val, res, end, cnt = len(nums), max(nums), 0, 0, 0
        for start in range(n):
            while end < n and cnt < k:
                if nums[end] == max_val: cnt += 1
                end += 1
            if cnt < k:
                return res
            res += n - end + 1
            if nums[start] == max_val: cnt -= 1
        return res