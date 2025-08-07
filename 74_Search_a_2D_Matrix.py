class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo = 0
        hi = m - 1
        row = None
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] > target:
                hi = mid - 1
            elif matrix[mid][-1] < target:
                lo = mid + 1
            else:
                row = mid
                break
        if row is None:
            row = lo
        idx = bisect_left(matrix[row], target)
        return idx < n and matrix[row][idx] == target