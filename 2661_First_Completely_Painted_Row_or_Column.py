class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        indices = {mat[i][j]: (i, j) for j in range(n) for i in range(m)}
        rows = [0] * m
        cols = [0] * n
        for i in range(len(arr)):
            x, y = indices[arr[i]]
            rows[x] += 1
            cols[y] += 1
            if rows[x] == n or cols[y] == m:
                return i
        