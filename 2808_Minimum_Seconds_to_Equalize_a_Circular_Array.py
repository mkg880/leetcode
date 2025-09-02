class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        m = {}
        for i, val in enumerate(nums):
            if val not in m:
                m[val] = []
            m[val].append(i)
        def sec(val):
            idx = m[val]
            res = (n - idx[-1] + idx[0]) // 2
            for i in range(1, len(idx)):
                res = max(res, (idx[i] - idx[i-1]) // 2)
            return res
        vis = set()
        res = float('inf')
        for val in nums:
            if val in vis:
                continue
            vis.add(val)
            res = min(res, sec(val))
        return res