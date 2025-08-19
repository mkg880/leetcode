class Solution:
    def minOperations(self, n: int) -> int:
        x = n // 2
        return x ** 2 if n % 2 == 0 else x ** 2 + x