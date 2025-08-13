class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        n = max([len(st) for st in arr])
        res = [''] * n
        last_ch = [-1] * n
        for i in range(len(arr)):
            for j in range(n):
                if j < len(arr[i]):
                    c = arr[i][j]
                    last_ch[j] = i
                else:
                    c = ' '
                res[j] += c
        return [st[:x+1] for st, x in zip(res, last_ch)]