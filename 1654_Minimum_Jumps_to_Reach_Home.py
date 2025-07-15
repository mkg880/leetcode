class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        stop = a + b + max(x, max(forbidden))
        f = set(forbidden)
        q = deque([(0, False, 0)])
        visited = set()
        while q:
            pos, back, dist = q.popleft()
            if pos in f or pos < 0 or pos > stop or (pos, back) in visited:
                continue
            visited.add((pos, back))
            if pos == x:
                return dist
            q.append((pos + a, False, dist + 1))
            if not back:
                q.append((pos - b, True, dist + 1))
        return -1