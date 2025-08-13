class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        res = set()
        vis = set()
        stack = [(0, set())]
        while stack:
            node, s = stack.pop()
            if node in vis:
                continue
            vis.add(node)
            if hasApple[node]:
                res.update(s)
            for neighbor in graph[node]:
                stack.append((neighbor, s | {(node, neighbor)}))
        return 2 * len(res)