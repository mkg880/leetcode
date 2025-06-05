class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if(len(digits) == 0):
            return res
        d = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'), '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}
        def rec(curr, i):
            for c in d[digits[i]]:
                s = curr + c
                if i == len(digits) - 1:
                    res.append(s)
                else:
                    rec(s, i + 1)
        rec("", 0)
        return res