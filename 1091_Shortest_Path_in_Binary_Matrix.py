class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        q.append((0, 0, 1))
        visited = set()
        while q:
            a, b, dist = q.popleft()
            if (a, b) in visited or grid[a][b] == 1:
                continue
            visited.add((a, b))
            if a == n-1 and b == n-1:
                return dist
            for i in range(max(0, a-1), min(n, a+2)):
                for j in range(max(0, b-1), min(n, b+2)):
                    if i == a and j == b:
                        continue
                    q.append((i, j, dist + 1))
        return -1