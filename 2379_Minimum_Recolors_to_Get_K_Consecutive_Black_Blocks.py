class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k-1
        cnt = 0
        for i in range(k):
            if blocks[i] == 'W':
                cnt += 1
        res = cnt
        while r+1 < len(blocks):
            if blocks[l] == 'W':
                cnt -= 1
            if blocks[r+1] == 'W':
                cnt += 1
            res = min(res, cnt)
            if res == 0:
                return 0
            r += 1
            l += 1
        return res