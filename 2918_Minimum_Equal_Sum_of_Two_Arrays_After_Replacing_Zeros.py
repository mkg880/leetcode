class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = sum(1 if x == 0 else 0 for x in nums1)
        z2 = sum(1 if x == 0 else 0 for x in nums2)
        s1, s2 = z1+sum(nums1), z2+sum(nums2)
        if (s1 < s2 and not z1) or (s2 < s1 and not z2):
            return -1
        return max(s1, s2)