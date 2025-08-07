class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for l in leaves:
                neighbor = list(graph[l])[0]
                graph[neighbor].remove(l)
                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves
        return leaves