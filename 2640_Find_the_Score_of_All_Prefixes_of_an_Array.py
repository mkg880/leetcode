class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        curr = 0
        m = 0
        res = []
        for i in range(len(nums)):
            m = max(m, nums[i])
            curr += m + nums[i]
            res.append(curr)
        return res