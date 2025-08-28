class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        pre = [[0]*(n+1) for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            for i in range(row1, row2+1):
                pre[i][col1] += 1
                pre[i][col2+1] -= 1
        curr = 0
        res = [[0]*(n) for _ in range(n)]
        for i in range(n):
            for j in range(n+1):
                curr += pre[i][j]
                if j < n:
                    res[i][j] = curr
        return res