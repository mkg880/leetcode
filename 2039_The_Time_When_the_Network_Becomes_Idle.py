class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        q = deque([(0, 0)])
        visited = set()
        dist = [0] * n
        while len(visited) < n and q:
            node, d = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            dist[node] = d
            for neighbor in graph[node]:
                q.append((neighbor, d+1))
        res = 0
        for d, p in zip(dist[1:], patience[1:]):
            time = d * 2
            if p >= time:
                val = time + 1
            else:
                resends = (time - 1) // p
                val = resends * p + time + 1
            res = max(res, val)
        return res