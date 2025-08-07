class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        r_cnt = 0
        d_cnt = 0
        for c in senate:
            q.append(c)
            if c == 'R':
                r_cnt += 1
            else:
                d_cnt += 1
        r_banned = 0
        d_banned = 0
        next_r = 0
        next_d = 0
        while r_banned < r_cnt and d_banned < d_cnt:
            party = q.popleft()
            if party == 'R' and next_r:
                next_r -= 1
            elif party == 'D' and next_d:
                next_d -= 1
            elif party == 'R':
                d_banned += 1
                next_d += 1
                q.append('R')
            else:
                r_banned += 1
                next_r += 1
                q.append('D')
        return 'Radiant' if r_banned < r_cnt else 'Dire'