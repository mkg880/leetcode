class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = [-1]
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        zeros.append(len(nums))
        if len(zeros) - 2 <= k:
            return len(nums)
        res = 0
        for i in range(k+1, len(zeros)):
            res = max(res, zeros[i] - zeros[i-k-1] - 1)
        return res