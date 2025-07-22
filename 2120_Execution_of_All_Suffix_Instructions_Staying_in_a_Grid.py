class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        moves = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
        res = []
        for i in range(m):
            y, x = startPos
            j = i
            while j < m:
                dx, dy = moves[s[j]]
                x, y = x + dx, y + dy
                if not (0 <= x < n and 0 <= y < n):
                    break
                j += 1
            res.append(j - i)
        return res