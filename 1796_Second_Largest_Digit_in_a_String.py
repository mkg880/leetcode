class Solution:
    def secondHighest(self, s: str) -> int:
        s = set([c for c in s if '9' >= c >= '0'])
        if len(s) < 2:
            return -1
        return int(sorted(list(s))[-2])