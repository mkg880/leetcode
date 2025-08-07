class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = ''
        curr = 0
        for i, c in enumerate(s[::-1]):
            curr += shifts[-i-1]
            n = ord(c) - ord('a')
            n = (n+curr) % 26
            res = chr(n + ord('a')) + res
        return res