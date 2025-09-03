class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        m = {}
        for i, val in enumerate(nums):
            if val not in m:
                m[val] = []
            m[val].append(i)
        res = 0
        for key in m:
            l = 0
            r = 0
            arr = m[key]
            while l < len(arr):
                while r < len(arr) and (arr[r] - arr[l]) - (r - l) <= k:
                    res = max(res, r - l + 1)
                    r += 1
                l += 1
        return res