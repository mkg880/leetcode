class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        m = {}
        for i, c in enumerate(s):
            if c not in m:
                m[c] = []
            m[c].append(i)
        ops = max(len(arr) for arr in m.values())
        x = sorted([(arr[-1], ch) for ch, arr in m.items() if len(arr) == ops])
        return ''.join([y[1] for y in x])