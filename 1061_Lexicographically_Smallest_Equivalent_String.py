class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = {}
        for a, b in zip(s1, s2):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        m = {}
        for x in graph:
            if x in visited:
                continue
            q = deque([x])
            minVal = x
            component = []
            while q:
                curr = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                component.append(curr)
                minVal = min(minVal, curr)
                for neighbor in graph.get(curr, []):
                    q.append(neighbor)
            for val in component:
                m[val] = minVal
        return "".join([m.get(c, c) for c in baseStr])