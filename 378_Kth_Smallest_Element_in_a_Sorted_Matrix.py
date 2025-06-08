class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def num_le(x):
            total = 0
            c = len(matrix)-1
            for row in matrix:
                while c >= 0 and row[c] > x:
                    c -= 1
                total += c+1
            return total
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if num_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo