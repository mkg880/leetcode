class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        l1, l2, l3, h1, h2, h3 = float('inf'), float('inf'), float('inf'), float('-inf'), float('-inf'), float('-inf')
        for val in nums:
            if val < l1: l1, l2, l3 = val, l1, l2
            elif val < l2: l2, l3 = val, l2
            elif val < l3: l3 = val
            if val > h1: h1, h2, h3 = val, h1, h2
            elif val > h2: h2, h3 = val, h2
            elif val > h3: h3 = val
        return min(h1 - l3, h2 - l2, h3 - l1)