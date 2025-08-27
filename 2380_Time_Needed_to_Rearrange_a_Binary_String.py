class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        res = 0
        z = 0
        for c in s:
            z += 1 if c == '0' else 0
            if c == '1' and z:
                res = max(res+1, z)
        return res