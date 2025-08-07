class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = 0
        for val in nums:
            if val % 2 == 0:
                evens += val
        res = []
        for val, idx in queries:
            new = nums[idx] + val
            if nums[idx] % 2 == 1 and new % 2 == 0:
                evens += new
            elif nums[idx] % 2 == 0 and new % 2 == 1:
                evens -= nums[idx]
            elif nums[idx] % 2 == 0 and new % 2 == 0:
                evens += val
            res.append(evens)
            nums[idx] = new
        return res