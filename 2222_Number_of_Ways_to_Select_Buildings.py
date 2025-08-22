class Solution:
    def numberOfWays(self, s: str) -> int:
        zero_one = 0
        one_zero = 0
        zeros = 0
        ones = 0
        res = 0
        for c in s:
            if c == '1':
                ones += 1
                res += one_zero
                zero_one += zeros
            else:
                zeros += 1
                res += zero_one
                one_zero += ones
        return res