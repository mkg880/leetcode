class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnts = {}
        for n in nums:
            cnts[n] = cnts.get(n, 0) + 1
        for key in cnts:
            if cnts[key] % 2 == 1:
                return False
        return True