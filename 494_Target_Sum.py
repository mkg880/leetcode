class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = {0: 1}
        for val in nums:
            temp = {}
            for key in m:
                temp[key + val] = temp.get(key + val, 0) + m[key]
                temp[key - val] = temp.get(key - val, 0) + m[key]
            m = temp
        return m.get(target, 0)
            