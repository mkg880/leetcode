from math import lcm, gcd
class Solution:
    def fractionAddition(self, expression: str) -> str:
        neg = 1
        i = 0
        nums = []
        dems = []
        if expression[0] == '-':
            neg = -1
            i = 1
        while i < len(expression):
            val = ''
            while expression[i].isdigit():
                val += expression[i]
                i += 1
            nums.append(int(val) * neg)
            i += 1
            val = ''
            while i < len(expression) and expression[i].isdigit():
                val += expression[i]
                i += 1
            dems.append(int(val))
            if i < len(expression):
                neg = 1 if expression[i] == '+' else -1
            i += 1
        d = lcm(*dems)
        print(dems)
        n = 0
        for i in range(len(nums)):
            n += nums[i] * (d / dems[i])
        n = int(n)
        g = gcd(n, d)
        if g != 1:
            n = int(n / g)
            d = int(d / g)
        return str(n) + "/" + str(d)

        