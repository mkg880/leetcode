class Solution:
    def minFlips(self, target: str) -> int:
        cnt = 0 
        curr = '1'
        for c in target:
            if c == curr:
                cnt += 1
                curr = '0' if curr == '1' else '1'
        return cnt