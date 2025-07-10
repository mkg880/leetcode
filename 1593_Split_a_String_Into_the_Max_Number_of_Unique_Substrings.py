class Solution:
    def rec(self, string: str, s: set, start: int):
        if start == len(string):
            return 0
        max = 0
        for i in range(start + 1, len(string) + 1):
            if string[start:i] in s:
                continue
            s.add(string[start:i])
            val = self.rec(string, s, i) + 1
            s.remove(string[start:i])
            if val > max:
                max = val
        return max
    def maxUniqueSplit(self, s: str) -> int:
        return self.rec(s, set(), 0)