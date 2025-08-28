class Solution:
    def prime_factors(self, n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for val in nums:
            f = self.prime_factors(val)
            for i in f:
                s.add(i)
        return len(s)