class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1 and nums[0] != val:
            return 1
        i = 0
        j = len(nums) - 1
        k = 0
        while i < j:
            while i < len(nums) and nums[i] != val:
                i+= 1
                k += 1
            while j >= 0 and nums[j] == val:
                j -= 1
            if i > j:
                return k
            else:
                nums[i] = nums[j]
                nums[j] = val
        return k
            