import heapq
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        res = 0
        n = len(nums)
        for i in range(n):
            while j < n and nums[j] == nums[i]:
                j += 1
            if j == n:
                return res
            res += 1
            j += 1
        return res