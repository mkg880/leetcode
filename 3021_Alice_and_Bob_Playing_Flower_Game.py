class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even_n, even_m = n // 2, m // 2
        odd_n, odd_m = even_n + 1 if n % 2 == 1 else even_n, even_m + 1 if m % 2 == 1 else even_m
        return odd_n * even_m + odd_m * even_n