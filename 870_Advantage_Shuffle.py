class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        temp = sorted((val, idx) for idx, val in enumerate(nums2))
        i, j = 0, 0
        m = {}
        avail = set(range(n))
        while i < n and j < n:
            val, idx = temp[j]
            while i < n and val >= nums1[i]:
                i += 1
            if i < n:
                m[idx] = i
                avail.remove(i)
            i += 1
            j += 1
        res = []
        it = iter(avail)
        for i in range(n):
            idx = m[i] if i in m else next(it)
            res.append(nums1[idx])
        return res