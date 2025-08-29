class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        stack = [(0, 0, [])]
        vis = set()
        found = None
        while stack:
            i, j, path = stack.pop()
            if (i, j) == (m-1, n-1):
                found = set(path)
                break
            if not 0 <= i < m or not 0 <= j < n or (i, j) in vis or not grid[i][j]:
                continue
            vis.add((i, j))
            temp = path + [(i, j)] if (i, j) != (0, 0) else path
            for x, y in ((i+1, j), (i, j+1)):
                stack.append((x, y, temp))
        if found is None:
            return True
        vis = found
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop()
            if (i, j) == (m-1, n-1):
                return False
            if not 0 <= i < m or not 0 <= j < n or (i, j) in vis or not grid[i][j]:
                continue
            vis.add((i, j))
            for x, y in ((i+1, j), (i, j+1)):
                stack.append((x, y))
        return True