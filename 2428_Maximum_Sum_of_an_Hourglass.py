class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        pre = []
        m, n = len(grid), len(grid[0])
        for row in grid:
            arr = []
            curr = 0
            for i in range(n):
                arr.append(curr)
                curr += row[i]
            arr.append(curr)
            pre.append(arr)
        res = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                curr = pre[i+1][j+2] - pre[i+1][j-1] + pre[i-1][j+2] - pre[i-1][j-1] + grid[i][j]
                res = max(res, curr)
        return res
        