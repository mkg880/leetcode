class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        vis = set()
        res = 0
        for i in range(n):
            if i in vis:
                continue
            stack = [i]
            prev = len(vis)
            v = 0
            while stack:
                x = stack.pop()
                if x in vis:
                    continue
                vis.add(x)
                v += len(graph[x])
                for neighbor in graph[x]:
                    stack.append(neighbor)
            e = len(vis) - prev
            if v == e * (e-1): res += 1
        return res