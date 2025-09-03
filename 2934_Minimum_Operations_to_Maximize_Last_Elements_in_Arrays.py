class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1 = 0
        cnt2 = 0
        for i in range(len(nums1) - 1):
            a = nums1[i]
            b = nums2[i]
            fixed = a <= nums1[-1] and b <= nums2[-1]
            swapped = a <= nums2[-1] and b <= nums1[-1]
            if not fixed and swapped:
                cnt1 += 1
            if not swapped and fixed:
                cnt2 += 1
            if not swapped and not fixed:
                return -1
        return min(cnt1, cnt2 + 1)