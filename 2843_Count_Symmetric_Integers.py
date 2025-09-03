class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for x in range(low, high + 1):
            s = str(x)
            if len(s) % 2 == 1:
                continue
            first = 0
            second = 0
            for c in range(len(s) // 2):
                first += int(s[c])
            for c in range(len(s) // 2, len(s)):
                second += int(s[c])
            if first == second:
                res += 1
        return res