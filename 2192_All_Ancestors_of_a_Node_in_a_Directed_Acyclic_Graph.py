class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for i in range(n)]
        graph = {i: [] for i in range(n)}
        indeg = [0 for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
        vis = set()
        start_nodes = [i for i in range(n) if indeg[i] == 0]
        order = []
        while start_nodes:
            node = start_nodes.pop(0)
            order.append(node)
            for neighbor in graph[node]:
                indeg[neighbor] -= 1
                if not indeg[neighbor]:
                    start_nodes.append(neighbor)
        ancestors = [set() for _ in range(n)]
        for node in order:
            for neighbor in graph[node]:
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])
        for i in range(n):
            for j in range(n):
                if j in ancestors[i]:
                    res[i].append(j)
        return res