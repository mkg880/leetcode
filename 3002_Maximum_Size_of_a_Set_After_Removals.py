class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1, s2 = set(nums1), set(nums2)
        c1, c2, common = set(), set(), set()
        for val in nums1:
            if val not in s2 and len(c1) < n // 2:
                c1.add(val)
            elif val in s2:
                common.add(val)
        for val in nums2:
            if val not in s1 and len(c2) < n // 2:
                c2.add(val)
        return min(len(c1) + len(c2) + len(common), n)