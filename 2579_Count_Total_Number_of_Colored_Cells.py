class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * (n-2) * (n-1) + 4 * n - 3