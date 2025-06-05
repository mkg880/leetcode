class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                board[a][b] = '-'
                for c, d in directions:
                    e, f = a + c, b + d
                    # print(f"checking {e, f}")
                    if e < len(board) and e >= 0 and f < len(board[0]) and f >= 0 and board[e][f] == 'O':
                        stack.append((e, f))
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][-1] == 'O':
                dfs(i, len(board[i]) - 1)
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[-1][j] == 'O':
                dfs(len(board) - 1, j)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'