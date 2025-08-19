class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        for val in nums:
            if val:
                res += cnt * (cnt+1) // 2
                cnt = 0
            else:
                cnt += 1
        res += cnt * (cnt+1) // 2
        return res