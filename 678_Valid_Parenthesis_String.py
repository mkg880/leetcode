class Solution:
    def checkValidString(self, s: str) -> bool:
        min = 0
        max = 0
        for c in s:
            if c == '(':
                min += 1
                max += 1
            elif c == ')':
                min -= 1
                max -= 1
            else:
                min -= 1
                max += 1
            if max < 0:
                return False
            if min < 0:
                min = 0
        return min == 0