class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a, b = firstList[i]
            c, d = secondList[j]
            max_start = max(a, c)
            min_end = min(b, d)
            if max_start <= min_end:
                res.append([max_start, min_end])
            if b <= d:
                i += 1
            if d <= b:
                j += 1
        return res