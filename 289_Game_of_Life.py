class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_state = []
        for i in range(len(board)):
            new_row = []
            for j in range(len(board[0])):
                neighbors = 0
                l_x = max(0, i - 1)
                l_y = max(0, j - 1)
                h_x = min(len(board), i + 2)
                h_y = min(len(board[0]), j + 2)
                for x in range(l_x, h_x):
                    for y in range(l_y, h_y):
                        if x == i and y == j:
                            continue
                        if board[x][y] == 1:
                            neighbors += 1
                if neighbors == 3 or (neighbors == 2 and board[i][j] == 1):
                    new_row.append(1)
                else:
                    new_row.append(0)
            new_state.append(new_row)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = new_state[i][j]