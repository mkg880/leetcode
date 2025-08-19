class Solution:
    def numWays(self, s: str) -> int:
        mod = 10 ** 9 + 7
        ones = []
        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)
        if len(ones) % 3 != 0:
            return 0
        if not ones:
            return (len(s) - 2) * (len(s) - 1) // 2 % mod
        x = len(ones) // 3
        l = ones[x] - ones[x-1]
        r = ones[-x] - ones[-x-1]
        return l * r % mod