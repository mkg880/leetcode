class Solution:
    def originalDigits(self, s: str) -> str:
        res = [0] * 10
        c = Counter(s)
        def unique(i, s, u):
            if not all(ch in c for ch in s):
                return
            n = c[u]
            res[i] += n
            del c[u]
            for ch in s:
                if ch == u:
                    continue
                c[ch] -= n
                if c[ch] == 0:
                    del c[ch]
        unique(0, 'zero', 'z')
        unique(2, 'two', 'w')
        unique(4, 'four', 'u')
        unique(6, 'six', 'x')
        unique(8, 'eight', 'g')
        unique(1, 'one', 'o')
        unique(3, 'three', 't')
        unique(5, 'five', 'f')
        unique(7, 'seven', 'v')
        unique(9, 'nine', 'i')
        return ''.join([str(i) * res[i] for i in range(10)])
