class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last_found = 0
        res = 0
        for row in bank:
            cnt = 0
            for c in row:
                if c == '1':
                    cnt += 1
            if cnt == 0:
                continue
            res += last_found * cnt
            last_found = cnt
        return res