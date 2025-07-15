class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = sum(nums1), sum(nums2)
        diff = abs(a - b)
        if not diff:
            return 0
        (bigger, smaller) = (nums1, nums2) if a > b else (nums2, nums1)
        b, s = {}, {}
        for val in bigger:
            b[val] = b.get(val, 0) + 1
        for val in smaller:
            s[val] = s.get(val, 0) + 1
        res = 0
        for i in range(1, 6):
            if diff <= 0:
                return res
            cnt = s.get(i, 0) + b.get(7-i, 0)
            val = ceil(diff / (6 - i))
            rem = min(cnt, val)
            diff -= rem * (6-i)
            res += rem
        if diff <= 0:
            return res
        else:
            return -1