class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(board, r, c):
            for i in range(c):
                if board[r][i] == 'Q':
                    return False
            for i, j in zip(range(r-1, -1, -1), range(c-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            for i, j in zip(range(r+1, n), range(c-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            return True
        res = []
        def rec(board, c):
            if c == n:
                res.append(deepcopy(board))
                return
            for i in range(n):
                if check(board, i, c):
                    board[i][c] = 'Q'
                    rec(board, c+1)
                    board[i][c] = '.'
        board = [['.' for j in range(n)] for i in range(n)]
        rec(board, 0)
        # print(res)
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = ''.join(res[i][j])
        return res