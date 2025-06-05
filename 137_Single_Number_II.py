class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = set(nums)
        found = set()
        for num in nums:
            if num in found and num in res:
                res.remove(num)
            found.add(num)
        (element,) = res
        return element