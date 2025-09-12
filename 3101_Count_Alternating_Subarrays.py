class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        prev = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                res += prev
                prev += 1
            else:
                prev = 1
        return res