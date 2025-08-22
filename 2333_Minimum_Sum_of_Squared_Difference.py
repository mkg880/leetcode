class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        arr = sorted([abs(x - y) for x, y in zip(nums1, nums2)])
        lo, hi = 0, max(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(max(0, val-mid) for val in arr) <= k:
                hi = mid
            else:
                lo = mid + 1
        k -= sum(max(0, val-lo) for val in arr)
        res = 0
        for val in arr:
            val = min(val, lo)
            if val == lo > 0 and k > 0:
                val -= 1
                k -= 1
            res += val ** 2
        return res