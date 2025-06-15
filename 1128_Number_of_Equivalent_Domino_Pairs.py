class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m = {}
        res = 0
        for a, b in dominoes:
            second = m.get((b, a), 0) if a != b else 0
            res += m.get((a, b), 0) + second
            m[(a, b)] = m.get((a, b), 0) + 1
        return res