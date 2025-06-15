class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        reds = {}
        blues = {}
        for a, b in redEdges:
            if a not in reds:
                reds[a] = []
            reds[a].append(b)
        for a, b in blueEdges:
            if a not in blues:
                blues[a] = []
            blues[a].append(b)
        res = [-1] * n
        q = deque([(0, True, 0), (0, False, 0)])
        visited = set()
        while q:
            node, red, dist = q.popleft()
            if (node, red) in visited:
                continue
            visited.add((node, red))
            if res[node] == -1 or dist < res[node]:
                res[node] = dist
            m = blues if red else reds
            for neighbor in m.get(node, []):
                q.append((neighbor, not red, dist + 1))
        return res
        