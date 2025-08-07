class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def rec(o, c):
            if o == c == n:
                res.append(''.join(stack))
            if o < n:
                stack.append('(')
                rec(o+1, c)
                stack.pop()
            if c < o:
                stack.append(')')
                rec(o, c+1)
                stack.pop()
        rec(0, 0)
        return res