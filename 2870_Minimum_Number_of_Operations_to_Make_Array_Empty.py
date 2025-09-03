class Solution:
    def minOperations(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if n not in m:
                m[n] = 0
            m[n] += 1
        cnt = 0
        for key in m:
            val = m[key]
            if val == 1:
                return -1
            if val >= 3:
                cnt += val // 3
                val = val % 3
            if val == 1:
                val = 4
                cnt -= 1
            if val >= 2:
                cnt += val // 2
        return cnt