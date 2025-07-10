class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        groups = [(1, n)]
        for i in range(n-1, -1, -1):
            idx = bisect_left(groups, (arr[i], n+1)) - 1
            start, end = groups[idx]
            if arr[i] == end:
                groups[idx] = (start, end - 1)
                if end - start == m:
                    return i
            elif arr[i] == start:
                groups[idx] = (start + 1, end)
                if end - start == m:
                    return i
            else:
                groups[idx] = (arr[i] + 1, end)
                if end - arr[i] == m:
                    return i
                groups.insert(idx, (start, arr[i] - 1))
                if arr[i] - start == m:
                    return i
        return -1