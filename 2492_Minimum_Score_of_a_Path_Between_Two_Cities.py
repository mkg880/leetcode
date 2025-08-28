class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b, dist in roads:
            graph[a-1].append((b-1, dist))
            graph[b-1].append((a-1, dist))
        stack = [0]
        vis = set()
        res = float('inf')
        while stack:
            node = stack.pop()
            if node in vis:
                continue
            vis.add(node)
            for neighbor, dist in graph[node]:
                res = min(res, dist)
                stack.append(neighbor)
        return res