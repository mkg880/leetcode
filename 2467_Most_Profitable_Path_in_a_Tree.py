from collections import deque
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = {}
        for a, b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        q = deque([(bob, [])])
        vis = set()
        while q:
            node, path = q.popleft()
            if node == 0:
                bob_path = path + [node]
                break
            if node in vis:
                continue
            vis.add(node)
            for neighbor in graph.get(node, []):
                q.append((neighbor, path + [node]))
        m = {bob_path[i]: i for i in range(len(bob_path))}
        stack = [(0, 0, 0)]
        res = float('-inf')
        vis = set()
        while stack:
            node, time, curr = stack.pop()
            if node in vis:
                continue
            vis.add(node)
            bob_time = m.get(node, float('inf'))
            if time < bob_time:
                curr += amount[node]
            elif time == bob_time:
                curr += amount[node] // 2
            neighbors = graph.get(node, [])
            if len(neighbors) == 1 and node != 0:
                res = max(res, curr)
            else:
                for neighbor in graph.get(node, []):
                    stack.append((neighbor, time+1, curr))
        return res