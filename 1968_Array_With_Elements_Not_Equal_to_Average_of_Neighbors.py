class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i % 2 == 0:
                res[i] = nums[i // 2]
            else:
                res[i] = nums[len(nums) - i // 2 - 1]
        return res
