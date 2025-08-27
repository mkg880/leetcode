class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        total = added = 0
        mask = 10
        while sum([int(c) for c in str(n)]) > target:
            added = mask - n % mask
            if added != mask:
                n += added
                total += added
            mask *= 10
        return total