class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        vis = set()
        id = list(range(n))
        for i in range(n):
            if i in vis:
                continue
            stack = [i]
            while stack:
                x = stack.pop()
                if x in vis:
                    continue
                vis.add(x)
                id[x] = i
                stack += graph[x]
        return len(set(id)) - 1