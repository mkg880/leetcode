class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        arr = sorted([(v, l) for v, l in zip(values, labels)], reverse=True)
        m = {}
        cnt = 0
        i = 0
        res = 0
        while i < len(arr) and cnt < numWanted:
            v, l = arr[i]
            if m.get(l, 0) == useLimit:
                i += 1
                continue
            res += v
            m[l] = m.get(l, 0) + 1
            cnt += 1
            i += 1
        return res