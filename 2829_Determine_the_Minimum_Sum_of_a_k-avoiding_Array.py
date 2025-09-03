class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        s = set()
        i = 1
        total = 0
        while len(s) < n:
            if k-i not in s:
                s.add(i)
                total += i
            i += 1
        return total