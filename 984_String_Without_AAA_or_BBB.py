class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        n = a+b
        curr = 'a' if a >= b else 'b'
        res = ''
        while len(res) < n:
            if len(res) > 1 and res[-1] == res[-2] == curr:
                curr = 'b' if curr == 'a' else 'a'
            res += curr
            if curr == 'a':
                a -= 1
            else:
                b -= 1
            curr = 'a' if a >= b else 'b'
        return res