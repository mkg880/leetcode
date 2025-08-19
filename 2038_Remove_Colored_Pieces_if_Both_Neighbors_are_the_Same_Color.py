class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        curr = colors[0]
        cnt = 1
        res = 0
        a, b = 0, 0
        for c in colors[1:]:
            if c == curr:
                cnt += 1
            else:
                if curr == 'A':
                    a += max(cnt-2, 0)
                else:
                    b += max(cnt-2, 0)
                cnt = 1
                curr = c
        if curr == 'A':
            a += max(cnt-2, 0)
        else:
            b += max(cnt-2, 0)
        return a > b