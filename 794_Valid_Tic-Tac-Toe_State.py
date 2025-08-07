class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        row = [[0, 0], [0, 0], [0, 0]]
        col = [[0, 0], [0, 0], [0, 0]]
        diag = [[0, 0], [0, 0]]
        x, o = 0, 0
        x_win, o_win = False, False
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    continue
                elif board[i][j] == 'X':
                    x += 1
                    row[i][0] += 1
                    col[j][0] += 1
                    if i == j:
                        diag[0][0] += 1
                    if i+j == 2:
                        diag[1][0] += 1
                    if row[i][0] == 3 or col[j][0] == 3 or diag[0][0] == 3 or diag[1][0] == 3:
                        x_win = True
                else:
                    o += 1
                    row[i][1] += 1
                    col[j][1] += 1
                    if i == j:
                        diag[0][1] += 1
                    if i+j == 2:
                        diag[1][1] += 1
                    if row[i][1] == 3 or col[j][1] == 3 or diag[0][1] == 3 or diag[1][1] == 3:
                        o_win = True
        if not o <= x <= o+1 or (x_win and o_win):
            return False
        return (x_win and x == o+1) or (o_win and x == o) or (not x_win and not o_win)