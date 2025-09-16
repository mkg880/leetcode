import math
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        m = {}
        for num in nums2:
            m[num*k] = m.get(num*k, 0) + 1
        res = 0
        for num in nums1:
            for val in range(1, int(math.sqrt(num)) + 1):
                if num % val == 0:
                    res += m.get(val, 0)
                    if num // val != val:
                        res += m.get(num // val, 0)
        return res