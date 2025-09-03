class Solution:
    def minimumSteps(self, s: str) -> int:
        whites = 0
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                res += whites
            else:
                whites += 1
        return res