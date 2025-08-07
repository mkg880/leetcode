class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                box_i, box_j = i // 3, j // 3
                val = board[i][j]
                if val == '.':
                    continue
                if val in rows[i] or val in cols[j] or val in boxes[box_i][box_j]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_i][box_j].add(val)
        return True