class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = {}
        res = []
        for val in nums:
            if val not in m:
                m[val] = 0
            m[val] += 1
        cutoff = len(nums) // 3
        for val in m:
            if m[val] > cutoff:
                res.append(val)
        return res