class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for val in nums:
            if len(stack) % 2 == 1 and stack[-1] == val:
                res += 1
            else:
                stack.append(val)
        if len(stack) % 2 == 1:
            res += 1
        return res