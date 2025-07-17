class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a = [i + 1 for i in range(n)]
        i = 0
        while len(a) > 1:
            i = (i + k - 1) % len(a)
            a.pop(i)
        return a[0]