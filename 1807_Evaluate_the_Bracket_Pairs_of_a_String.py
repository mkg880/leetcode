class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        m = {key: value for key, value in knowledge}
        start = 0
        left = s.find('(')
        res = ""
        while left != -1:
            res += s[start:left]
            right = s.find(')', left)
            key = s[left+1:right]
            res += m.get(key, '?')
            start = right + 1
            left = s.find('(', start)
        return res + s[start:]