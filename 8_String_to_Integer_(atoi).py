class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        neg = 1
        number = []
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
        if s[i] == '+' or s[i] == '-':
            neg = -1 if s[i] == '-' else 1
            i += 1
        while i < len(s) and s[i].isdigit():
            number.insert(0, ord(s[i]) - ord('0'))
            i += 1
        res = 0
        for i in range(len(number)):
            res += number[i] * (10 ** i) * neg
            if res > 2**31 - 1:
                return 2**31 - 1
            if res < -(2**31):
                return -(2**31)
        return res
            
        