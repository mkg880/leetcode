class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        labels = [-1] * n
        graph = {i: [] for i in range(n)}
        for x, y in paths:
            graph[x-1].append(y-1)
            graph[y-1].append(x-1)
        vis = set()
        for i in range(n):
            if i in vis:
                continue
            stack = [i]
            while stack:
                x = stack.pop()
                if x in vis:
                    continue
                vis.add(x)
                options = set(range(1, 5))
                for neighbor in graph[x]:
                    if labels[neighbor] in options:
                        options.remove(labels[neighbor])
                    stack.append(neighbor)
                labels[x] = next(iter(options))
        return labels