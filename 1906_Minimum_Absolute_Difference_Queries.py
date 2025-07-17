class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        m = {}
        res = []
        for i, val in enumerate(nums):
            if val not in m:
                m[val] = []
            m[val].append(i)
        for l, r in queries:
            vals = []
            for key in m:
                arr = m[key]
                a = bisect_left(arr, l)
                b = bisect_right(arr, r)
                if b > a:
                    vals.append(key)
            vals.sort()
            min_val = float('inf')
            for i in range(1, len(vals)):
                diff = vals[i] - vals[i-1]
                if diff:
                    min_val = min(min_val, diff)
            res.append(-1 if min_val == float('inf') else min_val)
        return res