class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        q = deque()
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 0:
                    isWater[i][j] = float('inf')
                else:
                    isWater[i][j] = 0
                    q.append((i, j))
        while q:
            a, b = q.popleft()
            for c, d in neighbors:
                e, f = a + c, b + d
                if e >= 0 and e < m and f >= 0 and f < n and isWater[e][f] > isWater[a][b] + 1:
                    isWater[e][f] = isWater[a][b] + 1
                    q.append((e, f))
        return isWater