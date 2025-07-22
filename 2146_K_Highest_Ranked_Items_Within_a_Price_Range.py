class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        low, hi = pricing
        q = deque([(start[0], start[1], 0)])
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis = set()
        res = []
        while q:
            x, y, d = q.popleft()
            if not (0 <= x < m and 0 <= y < n):
                continue
            val = grid[x][y]
            if val == 0 or (x, y) in vis:
                continue
            vis.add((x, y))
            if low <= val <= hi:
                res.append((d, val, x, y))
            for dx, dy in dir:
                q.append((x+dx, y+dy, d+1))
        res.sort()
        res = res[:k]
        return [[x, y] for _, _, x, y in res]