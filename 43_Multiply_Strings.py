class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = [0] * 400
        n, m = len(num1), len(num2)
        for i in range(n):
            carry = 0
            c1 = ord(num1[n-i-1]) - ord('0')
            for j in range(m):
                c2 = ord(num2[m-j-1]) - ord('0')
                val = c1 * c2
                place = 400 - (i+j) - 1
                carry = val // 10
                digits[place] += (val % 10)
                carry += digits[place] // 10
                digits[place] %= 10
                digits[place-1] += carry
        start = 0
        while start < 400 and digits[start] == 0:
            start += 1
        if start == 400:
            return '0'
        return "".join([str(x) for x in digits[start:]])