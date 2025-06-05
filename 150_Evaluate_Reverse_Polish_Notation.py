class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    val = a + b
                elif i == '-':
                    val = b - a
                elif i == '*':
                    val = a * b
                else:
                    val = int(float(b) / float(a))
                stack.append(val)
        return stack.pop()