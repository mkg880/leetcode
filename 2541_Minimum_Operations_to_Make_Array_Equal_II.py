class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        diff = [a-b for a, b in zip(nums1, nums2)]
        if k == 0:
            return -1 if any(diff) else 0
        inc = 0
        dec = 0
        for d in diff:
            if d % k != 0:
                return -1
            if d > 0:
                inc += d // k
            else:
                dec -= d // k
        return inc if inc == dec else -1