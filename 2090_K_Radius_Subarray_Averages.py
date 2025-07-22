class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= 2*k:
            return [-1] * n
        res = [-1] * k
        total = sum(nums[:2*k+1])
        start = 0
        for i in range(n-2*k):
            avg = total // (2*k+1)
            res.append(avg)
            total -= nums[start]
            start += 1
            if i != n-2*k-1:
                total += nums[2*k+start]
        res += [-1] * k
        return res