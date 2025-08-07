class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def translate(x):
            row = -((x-1) // n) - 1
            col = (x-1) % n
            if row % 2 == 0:
                col = -col - 1
            return (row, col)
        q = deque([(1, 0)])
        vis = set()
        while q:
            curr, d = q.popleft()
            if curr == n ** 2:
                return d
            if curr in vis:
                continue
            vis.add(curr)
            for x in range(curr + 1, min(curr + 6, n ** 2) + 1):
                i, j = translate(x)
                if board[i][j] == -1:
                    q.append((x, d+1))
                else:
                    q.append((board[i][j], d+1))
        return -1

