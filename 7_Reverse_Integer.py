class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        rev = str(x)
        if rev[0] == '-':
            neg = True
            rev = rev[1:]
        rev = rev[::-1]
        if neg:
            rev = '-' + rev
        res = int(rev)
        if res.bit_length() < 32:
            return res
        return 0