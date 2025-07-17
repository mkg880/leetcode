class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        arr = sorted(nums1)
        def bin_search(target):
            res = arr[0]
            lo = 0
            hi = len(arr) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if abs(arr[mid] - target) < abs(res - target):
                    res = arr[mid]
                elif abs(arr[mid] - target) == abs(res - target):
                    res = max(res, arr[mid])
                if arr[mid] == target:
                    return arr[mid]
                elif arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return res
        curr_sum = 0
        for a, b in zip(nums1, nums2):
            curr_sum += abs(a - b)
        closest_vals = [bin_search(val) for val in nums2]
        best = 0
        for i in range(len(nums1)):
            diff = abs(closest_vals[i] - nums2[i]) - abs(nums2[i] - nums1[i])
            best = min(best, diff)
        return (curr_sum + best) % (10**9 + 7)