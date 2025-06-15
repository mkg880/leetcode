class Solution:
    def clumsy(self, n: int) -> int:
        op = 0
        res = str(n)
        n -= 1
        operations = [' * ', ' // ', ' + ', ' - ']
        while n > 0:
            res += operations[op % 4] + str(n)
            n -= 1
            op += 1
        return eval(res)