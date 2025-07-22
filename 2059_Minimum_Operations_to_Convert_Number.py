class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        def add(a, b):
            return a + b
        def sub(a, b):
            return a - b
        def xor(a, b):
            return a ^ b
        ops = [add, sub, xor]
        visited = set()
        q = deque([(start, 0)])
        while q:
            a, dist = q.popleft()
            if a == goal:
                return dist
            if a in visited or not 0 <= a <= 1000:
                continue
            visited.add(a)
            for op in ops:
                for b in nums:
                    x = op(a, b)
                    q.append((x, dist + 1))
        return -1