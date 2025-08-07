class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        dec = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if i == 1 or i == len(nums) - 1 or nums[i] >= nums[i-2] or nums[i+1] >= nums[i-1]:
                    if dec:
                        return False
                    dec = True
                else:
                    return False
        return True