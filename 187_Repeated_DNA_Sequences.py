class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        curr = s[:10]
        m = {}
        m[curr] = 1
        for i in range(10, len(s)):
            curr = curr[1:] + s[i]
            m[curr] = m.get(curr, 0) + 1
        return [key for key in m if m[key] > 1]