class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a, b = pattern
        curr = 0
        first, second = 0, 0
        res = 0
        for c in text:
            if c == b:
                second += 1
                res += curr
            if c == a:
                first += 1
                curr += 1
        return res + max(first, second)