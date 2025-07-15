class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        m = {}
        for a, b in adjacentPairs:
            if a not in m:
                m[a] = []
            if b not in m:
                m[b] = []
            m[a].append(b)
            m[b].append(a)
        res = []
        for key in m:
            if len(m[key]) == 1:
                prev = key
                break
        res.append(prev)
        curr = m[prev][0]
        while len(m[curr]) == 2:
            res.append(curr)
            temp = sum(m[curr]) - prev
            prev = curr
            curr = temp
        res.append(curr)
        return res