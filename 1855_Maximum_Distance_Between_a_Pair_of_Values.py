class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        i = 0
        for j in range(len(nums2)):
            while i < len(nums1) and nums2[j] < nums1[i]:
                i += 1
            if i == len(nums1):
                break
            res = max(res, j - i)
        return res