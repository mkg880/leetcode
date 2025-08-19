from math import ceil
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0] * (limit * 2 + 2)
        n = len(nums)
        for i in range(n // 2):
            x, y = nums[i], nums[n-i-1]
            min_total = min(x, y) + 1
            max_total = max(x, y) + limit
            diff[2] += 2
            diff[min_total] -= 1
            diff[x+y] -= 1
            diff[x+y+1] += 1
            diff[max_total+1] += 1
        res = diff[2]
        curr = diff[2]
        for i in range(3, len(diff)):
            curr += diff[i]
            res = min(res, curr)
        return res