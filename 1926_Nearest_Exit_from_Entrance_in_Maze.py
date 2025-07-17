class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        queued = set()
        while q:
            x, y, dist = q.popleft()
            if (x == 0 or y == 0 or x == m - 1 or y == n - 1) and [x, y] != entrance:
                return dist
            maze[x][y] = '+'
            for d_x, d_y in directions:
                a, b = x + d_x, y + d_y
                if a < 0 or b < 0 or a >= m or b >= n or maze[a][b] == '+' or (a, b) in queued:
                    continue
                q.append((a, b, dist+1))
                queued.add((a, b))
        return -1