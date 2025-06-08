class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        m = {}
        for i in range(n):
            m[s[i]] = i
        i = 0
        start = 0
        curr = m[s[0]]
        res = []
        while i < n:
            if i > curr:
                res.append(i - start)
                curr = m[s[i]]
                start = i
            else:
                curr = max(curr, m[s[i]])
                i += 1
        res.append(i - start)
        return res 