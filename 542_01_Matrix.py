class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = float('inf')
                else:
                    q.append((i, j))
        while q:
            a, b = q.popleft()
            for c, d in neighbors:
                e, f = a + c, b + d
                if e >= 0 and e < m and f >= 0 and f < n and mat[e][f] > mat[a][b] + 1:
                    mat[e][f] = mat[a][b] + 1
                    q.append((e, f))
        return mat