class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        stack = [[]]
        while stack:
            arr = stack.pop()
            if len(arr) == n:
                res.append(arr)
                continue
            s = set(arr)
            for i in range(n):
                if nums[i] not in s:
                    stack.append(arr + [nums[i]])
        return res