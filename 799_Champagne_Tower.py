class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[poured]]
        for i in range(1, query_row):
            arr = []
            for j in range(i+1):
                curr = 0
                if j-1 >= 0 and dp[i-1][j-1] > 1:
                    curr += (dp[i-1][j-1] - 1) / 2
                if j < i and dp[i-1][j] > 1:
                    curr += (dp[i-1][j] - 1) / 2
                arr.append(curr)
            dp.append(arr)
        return min(dp[query_row][query_glass], 1)
        