class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        arr = []
        for start, end in intervals:
            arr.append((start, 1))
            arr.append((end+1, -1))
        arr.sort()
        res = 0
        curr = 0
        for _, val in arr:
            curr += val
            res = max(res, curr)
        return res