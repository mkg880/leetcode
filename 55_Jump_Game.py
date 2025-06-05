class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for i in range(len(nums)):
            if curr < i:
                return False
            curr = max(curr, i + nums[i])
        return True