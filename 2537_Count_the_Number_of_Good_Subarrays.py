class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = {}
        end = -1
        cnt = 0
        res = 0
        for start in range(n):
            while end+1 < n and cnt < k:
                end += 1
                curr = m.get(nums[end], 0)
                cnt += curr
                m[nums[end]] = curr + 1
            if cnt >= k:
                res += n-end
            m[nums[start]] -= 1
            cnt -= m[nums[start]]
        return res