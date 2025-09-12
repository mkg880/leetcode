class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n, m = len(nums1), len(nums2)
        def possible(x):
            i, j, found = 0, 0, 0
            while i < n and j < m:
                if nums1[i] + x == nums2[j]:
                    j += 1
                else:
                    found += 1
                    if found > 2:
                        return False
                i += 1
            return True
        mi2 = nums2[0]
        res = float('inf')
        for val in nums1[:3]:
            if possible(mi2 - val):
                res = min(res, mi2 - val)
        return res