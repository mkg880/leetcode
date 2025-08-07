class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        remaining = Counter(nums)
        ending = {}
        for val in nums:
            if not remaining[val]:
                continue
            if val-1 in ending and ending[val-1]:
                ending[val-1] -= 1
                ending[val] = ending.get(val, 0) + 1
                remaining[val] -= 1
            elif remaining[val+1] and remaining[val+2]:
                remaining[val] -= 1
                remaining[val+1] -= 1
                remaining[val+2] -= 1
                ending[val+2] = ending.get(val+2, 0) + 1
            else:
                return False
        return True