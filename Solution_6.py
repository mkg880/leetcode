class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = []
        for i in range(numRows):
            arr.append('')
        d = 1
        i = 0
        for c in range(len(s)):
            arr[i] += s[c]
            if (i == 0 and d == -1) or (i == numRows - 1 and d == 1):
                d *= -1
            i += d
        res = ''
        for a in arr:
            res += a
        return res
                