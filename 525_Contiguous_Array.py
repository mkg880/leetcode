class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m = {}
        cnt = 0
        res = 0
        for i in range(len(nums)):
            cnt += 1 if nums[i] == 1 else -1
            if cnt == 0:
                res = max(res, i + 1)
            elif cnt in m:
                res = max(res, i - m[cnt])
            else:
                m[cnt] = i
        return res