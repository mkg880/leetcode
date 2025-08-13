from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        nums.sort()
        c = Counter(nums)
        for val in nums:
            if c[val] == 0:
                continue
            for x in range(val, val+k):
                if c[x] == 0:
                    return False
                c[x] -= 1
        return True
