class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        z = 0
        high = 0
        res = []
        for i in range(n+1):
            o = total - (i - z)
            score = o + z
            if score > high:
                high = score
                res = [i]
            elif score == high:
                res.append(i)
            if i < n and nums[i] == 0:
                z += 1
        return res