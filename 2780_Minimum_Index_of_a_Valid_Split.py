from typing import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        c = Counter(nums)
        for key, val in c.items():
            if val > n // 2:
                dom, cnt = key, val
                break
        found = 0
        for i in range(n):
            if nums[i] == dom: found += 1
            if found > (i+1) // 2 and cnt-found > (n-i-1) // 2:
                return i
        return -1