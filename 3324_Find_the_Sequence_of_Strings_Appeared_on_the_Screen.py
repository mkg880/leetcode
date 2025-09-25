class Solution:
    def stringSequence(self, target: str) -> List[str]:
        s = []
        res = []
        i = 0
        while i < len(target):
            if len(s) == i:
                s.append('a')
                res.append(''.join(s))
            elif s[i] == target[i]:
                i += 1
            else:
                s[-1] = chr(ord(s[-1]) + 1)
                res.append(''.join(s))
        return res