class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        n = len(nums)
        curr = 0
        i = 0
        while i < n:
            m = len(groups[curr])
            if nums[i:i+m] == groups[curr]:
                curr += 1
                i += m
                if curr == len(groups):
                    return True
            else:
                i += 1
        return False