class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if word[0] != board[-1]:
            first, last = 0, 0
            for c in word:
                if c == word[0]:
                    first += 1
                if c == word[-1]:
                    last += 1
            if first > last:
                word = word[::-1]
        vis = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def rec(i, j, k):
            if k == len(word):
                return True
            if not 0 <= i < m or not 0 <= j < n or (i, j) in vis or board[i][j] != word[k]:
                return False
            vis.add((i, j))
            for di, dj in dirs:
                if rec(i+di, j+dj, k+1):
                    return True
            vis.remove((i, j))
            return False
        for i in range(m):
            for j in range(n):
                if rec(i, j, 0):
                    return True
        return False