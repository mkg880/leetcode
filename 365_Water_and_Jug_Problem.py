class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()
        q = deque()
        q.append((0, 0))
        while q:
            a, b = q.popleft()
            if (a, b) in visited:
                continue
            if a + b == target:
                return True
            visited.add((a, b))
            q.append((x, b))
            q.append((a, y))
            q.append((0, b))
            q.append((a, 0))
            t1 = min(a, y - b)
            t2 = min(x - a, b)
            q.append((a - t1, b + t1))
            q.append((a + t2, b - t2))
        return False