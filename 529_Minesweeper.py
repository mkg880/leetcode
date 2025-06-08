class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def reveal(i, j):
            if board[i][j] != 'E':
                return
            adj = 0
            for a in range(max(i-1, 0), min(i+2, len(board))):
                for b in range(max(j-1, 0), min(j+2, len(board[i]))):
                    if board[a][b] in ['M', 'X']:
                        adj += 1
            if adj:
                board[i][j] = str(adj)
            else:
                board[i][j] = 'B'
                for a in range(max(i-1, 0), min(i+2, len(board))):
                    for b in range(max(j-1, 0), min(j+2, len(board[i]))):
                        if a == i and b == j:
                            continue
                        reveal(a, b)
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
        else:
            reveal(i, j)
        return board
            