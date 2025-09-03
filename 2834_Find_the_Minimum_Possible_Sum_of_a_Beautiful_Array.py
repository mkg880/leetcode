class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 10 ** 9 + 7
        temp = target // 2
        if temp >= n:
            return (n * (n+1) // 2) % mod
        total = temp * (temp + 1) // 2
        temp = n - temp
        temp2 = target + temp - 1
        add = temp2 * (temp2 + 1) // 2
        sub = target * (target - 1) // 2
        return (total + add - sub) % mod
