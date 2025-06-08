class Solution:
    def recurse(self, row, col, idx, visited):
        if idx > self.k:
            return 1
        if row < 0 or row >= self.n or col < 0 or col >= self.n:
            return 0
        if (row, col, self.k - idx) in visited:
            return visited[(row, col, self.k - idx)]
        total = 0
        for (i, j) in self.possibilities:
            new_row = row + i
            new_col = col + j
            total += self.recurse(new_row, new_col, idx+1, visited)
        total = total / 8
        visited[(row, col, self.k - idx)] = total
        return total
                
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.n = n
        self.k = k
        self.possibilities = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        return self.recurse(row, column, 0, {})
        