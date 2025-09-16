class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        m = len(nums)
        n = len(str(nums[0]))
        arr = [{} for _ in range(n)]
        for num in nums:
            s = str(num)
            for i in range(len(s)):
                arr[i][s[i]] = arr[i].get(s[i], 0) + 1
        res = 0
        for d in arr:
            for val in d.values():
                res += val * (m - val)
        return res