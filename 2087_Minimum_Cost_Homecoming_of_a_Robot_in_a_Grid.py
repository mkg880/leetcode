class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        start_row, start_col = startPos
        end_row, end_col = homePos
        total_row = sum(rowCosts[start_row+1:end_row+1]) if start_row <= end_row else sum(rowCosts[end_row:start_row])
        total_col = sum(colCosts[start_col+1:end_col+1]) if start_col <= end_col else sum(colCosts[end_col:start_col])
        return total_row + total_col