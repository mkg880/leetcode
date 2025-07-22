class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def cmp(x):
            s = str(x)
            res = ''
            for c in s:
                res += str(mapping[int(c)])
            return int(res)
        return sorted(nums, key=cmp)