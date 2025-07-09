class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        m = {}
        res = []
        for i, val in enumerate(groupSizes):
            if val not in m:
                m[val] = [i]
            else:
                m[val].append(i)
            if len(m[val]) == val:
                res.append(m[val])
                del m[val]
        return res