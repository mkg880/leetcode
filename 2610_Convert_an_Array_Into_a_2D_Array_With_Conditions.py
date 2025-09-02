from typing import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        m = Counter(nums)
        res = []
        while True:
            curr = []
            for key in m:
                if not m[key]:
                    continue
                curr.append(key)
                m[key] -= 1
            if curr:
                res.append(curr)
            else:
                break
        return res