class Solution:
    def lengthLongestPath(self, input: str) -> int:
        arr = input.split('\n')
        stack = []
        res = 0
        for s in arr:
            tabs = 0
            while s[tabs] == '\t':
                tabs += 1
            pops = len(stack) - tabs
            for _ in range(pops):
                stack.pop()
            if '.' in s:
                length = sum([len(x) for x in stack]) + len(s) - tabs
                res = max(res, length)
            else:
                stack.append(s[tabs:] + '/')
        return res