class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        (better, worse) = (('a', 'b'), ('b', 'a')) if x > y else (('b', 'a'), ('a', 'b'))
        stack = []
        a, b = 0, 0
        for c in s:
            if stack and (stack[-1], c) == better:

                stack.pop()
                a += 1
            else:
                stack.append(c)
        stack2 = []
        for c in stack:
            if stack2 and (stack2[-1], c) == worse:
                stack2.pop()
                b += 1
            else:
                stack2.append(c)
        return a * max(x, y) + b * min(x, y)