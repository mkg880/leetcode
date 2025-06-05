class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0.0
        def rec(v, p):
            if p == 0:
                return 1
            a = rec(v, p // 2)
            a *= a
            if p % 2 == 1:
                a *= v
            return a
        res = rec(x, abs(n))
        if n < 0:
            return 1/res
        return res