class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        m = {}
        res = [0] * len(arr)
        for i, val in enumerate(arr):
            if val not in m:
                m[val] = []
            m[val].append(i)
        for key in m:
            before = 0
            after = sum(m[key])
            for i, val in enumerate(m[key]):
                after -= val
                amt = (-val * (len(m[key]) - i - 1)) + (val * i)
                res[val] = before + after + amt
                before -= val
        return res