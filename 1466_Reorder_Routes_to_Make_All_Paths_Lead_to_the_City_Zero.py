class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, True))
            graph[b].append((a, False))
        stack = [0]
        vis = set()
        res = 0
        while stack:
            node = stack.pop()
            vis.add(node)
            for neighbor, direction in graph[node]:
                if neighbor in vis:
                    continue
                if direction:
                    res += 1
                stack.append(neighbor)
        return res