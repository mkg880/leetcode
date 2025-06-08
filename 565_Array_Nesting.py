class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for val in nums:
            curr = 0
            while nums[val] >= 0:
                temp = nums[val]
                nums[val] = -1
                val = temp
                curr += 1
            res = max(res, curr)
        return res