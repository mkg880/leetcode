class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        m = {nums[i]: i for i in range(len(nums))}
        for old, new in operations:
            i = m[old]
            nums[i] = new
            m[new] = i
        return nums