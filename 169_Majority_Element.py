class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for val in nums:
            if val not in m:
                m[val] = 0
            m[val] += 1
            if m[val] > len(nums) // 2:
                return val