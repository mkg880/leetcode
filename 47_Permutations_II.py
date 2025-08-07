class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cnts = Counter(nums)
        res = []
        def rec(arr):
            if len(arr) == len(nums):
                res.append(arr)
                return
            for val in cnts:
                if cnts[val] == 0:
                    continue
                cnts[val] -= 1
                rec(arr + [val])
                cnts[val] += 1
        rec([])
        return res