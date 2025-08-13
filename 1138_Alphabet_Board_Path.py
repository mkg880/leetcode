class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        m = {}
        for i in range(26):
            c = chr(i + ord('a'))
            m[c] = [i // 5, i % 5]
        prev = 'a'
        res = ''
        for c in target:
            x1, y1 = m[prev]
            x2, y2 = m[c]
            dx, dy = x2-x1, y2-y1
            if c == 'z':
                if dy < 0:
                    res += 'L' * -dy
                else:
                    res += 'R' * dy
                dy = 0
            if dx < 0:
                res += 'U' * -dx
            else:
                res += 'D' * dx
            if dy < 0:
                res += 'L' * -dy
            else:
                res += 'R' * dy
            res += '!'
            prev = c
        return res