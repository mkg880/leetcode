class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        ones = sum(possible)
        bob = 2 * ones - n
        alice = 0
        for i in range(n-1):
            if possible[i]:
                alice += 1
                bob -= 1
            else:
                alice -= 1
                bob += 1
            if alice > bob:
                return i + 1
        return -1