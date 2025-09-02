class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(k):
            if nums[i] < 0:
                m[nums[i]] = m.get(nums[i], 0) + 1
        res = []
        for i in range(n-k+1):
            cnt = 0
            val = 0
            for j in range(-50, 0):
                cnt += m.get(j, 0)
                if cnt >= x:
                    val = j
                    break
            res.append(val)
            if nums[i] in m:
                m[nums[i]] -= 1
            if i+k < n and nums[i+k] < 0:
                m[nums[i+k]] = m.get(nums[i+k], 0) + 1
        return res