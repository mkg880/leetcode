class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        m = {i: set() for i in range(n)}
        for a, b in roads:
            m[a].add(b)
            m[b].add(a)
        res = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                amt = len(m[i]) + len(m[j])
                if j in m[i]:
                    amt -= 1
                res = max(res, amt)
        return res