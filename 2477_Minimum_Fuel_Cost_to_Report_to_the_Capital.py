from math import ceil
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        res = 0
        def dfs(node, prev):
            nonlocal res
            cnt = 1
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                cnt += dfs(neighbor, node)
            if node != 0:
                res += ceil(cnt / seats)
            return cnt
        dfs(0, None)
        return res