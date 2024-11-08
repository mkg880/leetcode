class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = {0: -1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            total = total % k
            if total in m and i - m[total] >= 2:
                return True
            if total not in m:
                m[total] = i
        return False