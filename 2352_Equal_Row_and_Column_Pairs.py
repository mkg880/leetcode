class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {}
        for arr in grid:
            t = tuple(arr)
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
        total = 0
        for i in range(0, len(grid)):
            col = tuple([row[i] for row in grid])
            if col in d:
                total += d[col]
        return total