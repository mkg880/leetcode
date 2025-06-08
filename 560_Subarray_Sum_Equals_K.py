class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnts = {0: 1}
        curr = 0
        res = 0
        for n in nums:
            curr += n
            diff = curr - k
            res += cnts.get(diff, 0)
            if curr not in cnts:
                cnts[curr] = 0
            cnts[curr] += 1
        return res