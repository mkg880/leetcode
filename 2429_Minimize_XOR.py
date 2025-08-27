class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b = format(num2, 'b')
        num = b.count('1')
        b2 = format(num1, 'b')
        # print(b, b2)
        i = 0
        cnt = 0
        res = []
        stack = []
        while i < len(b2):
            if b2[i] == '1' and cnt < num:
                res.append('1')
                cnt += 1
            else:
                res.append('0')
                stack.append(i)
            i += 1
        while cnt < num:
            if stack:
                idx = stack[-1]
                stack.pop()
                res[idx] = '1'
            else:
                res = ['1'] + res
            cnt += 1
        res_str = ''.join(res)
        return int(res_str, 2)