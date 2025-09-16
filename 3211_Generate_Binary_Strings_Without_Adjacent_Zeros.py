class Solution:
    def validStrings(self, n: int) -> List[str]:
        stack = ['0', '1']
        res = []
        while stack:
            s = stack.pop()
            if len(s) == n:
                res.append(s)
                continue
            stack.append(s + '1')
            if s[-1] == '1':
                stack.append(s + '0')
        return res