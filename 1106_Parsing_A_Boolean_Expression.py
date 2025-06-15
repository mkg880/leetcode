class Solution:
    def parseBoolExprHelper(self, expression: str) -> bool:
        c = expression[self.i]
        self.i += 1
        if c == 't':
            return True
        if c == 'f':
            return False
        if c == '!':
            self.i += 1
            b = self.parseBoolExprHelper(expression)
            self.i += 1
            return not b
        else:
            arr = []
            self.i += 1
            while expression[self.i] != ')':
                if expression[self.i] == ',':
                    self.i += 1
                else:
                    arr.append(self.parseBoolExprHelper(expression))
            self.i += 1
            if c == '&':
                return all(arr)
            else:
                return any(arr)

    def parseBoolExpr(self, expression: str) -> bool:
        self.i = 0
        return self.parseBoolExprHelper(expression)