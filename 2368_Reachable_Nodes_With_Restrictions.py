from collections import deque
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = {}
        for a, b in edges:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
            if b not in graph:
                graph[b] = []
            graph[b].append(a)
        vis = set(restricted)
        q = deque([0])
        res = 0
        while q:
            node = q.popleft()
            if node in vis:
                continue
            res += 1
            vis.add(node)
            q.extend(graph.get(node, []))
        return res