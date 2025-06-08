class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        res = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.' or (i, j) in visited:
                    continue
                a = i
                while a < len(board) and board[a][j] == 'X':
                    visited.add((a, j))
                    a += 1
                b = j
                while b < len(board[i]) and board[i][b] == 'X':
                    visited.add((i, b))
                    b += 1
                res += 1
        return res