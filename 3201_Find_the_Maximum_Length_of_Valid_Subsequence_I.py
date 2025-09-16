class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd, even, alt = 0, 0, 0
        prev = None
        for val in nums:
            mod = val % 2
            if mod == 0:
                even += 1
            else:
                odd += 1
            if prev != mod:
                alt += 1
            prev = mod
        return max(odd, even, alt)