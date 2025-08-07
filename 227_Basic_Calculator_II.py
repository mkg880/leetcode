class Solution:
    def calculate(self, s: str) -> int:
        def getNum(i):
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            val = int(s[start:i])
            return val, i

        s = s.replace(" ", "")
        ops = []
        nums = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                val, i = getNum(i)
                nums.append(val)
            elif c in ['+', '-']:
                ops.append(c)
                i += 1
            else:
                op1 = nums.pop()
                op2, i = getNum(i+1)
                if c == '*':
                    val = op1 * op2
                else:
                    val = op1 // op2
                nums.append(val)
        res = 0
        while ops:
            op = ops.pop()
            num = nums.pop()
            if op == '+':
                res += num
            else:
                res -= num
        return nums.pop() + res