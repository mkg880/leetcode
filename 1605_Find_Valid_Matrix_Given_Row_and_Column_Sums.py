class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]
        curr_row = [0] * m
        curr_col = [0] * n
        for i in range(m):
            for j in range(n):
                res[i][j] = min(rowSum[i] - curr_row[i], colSum[j] - curr_col[j])
                curr_row[i] += res[i][j]
                curr_col[j] += res[i][j]
        return res