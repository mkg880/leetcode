class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = {}
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            id1 = nums1[i][0] if i < len(nums1) else float('inf')
            id2 = nums2[j][0] if j < len(nums2) else float('inf')
            if id1 < id2:
                m[id1] = m.get(id1, 0) + nums1[i][1]
                i += 1
            else:
                m[id2] = m.get(id2, 0) + nums2[j][1]
                j += 1
        return list(m.items())