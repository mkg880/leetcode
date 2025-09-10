class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        res = 0
        for i in range(n-m):
            valid = True
            for k in range(m):
                d = nums[i+k+1] - nums[i+k]
                if (d > 0 and pattern[k] <= 0) or (d == 0 and pattern[k] != 0) or (d < 0 and pattern[k] >= 0):
                    valid = False
                    break
            if valid: res += 1
        return res