class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ops = 0
        curr = nums[0]
        res = 0
        for val in nums[1:]:
            if val != curr:
                ops += 1
            curr = val
            res += ops
        return res