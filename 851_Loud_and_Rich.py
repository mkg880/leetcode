class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = {i: [] for i in range(n)}
        indeg = [0] * n
        for a, b in richer:
            graph[b].append(a)
            indeg[a] += 1

        res = list(range(n))

        def dfs(node):
            if res[node] != node:
                return res[node]
            ret = res[node]
            for neighbor in graph[node]:
                curr = dfs(neighbor)
                if quiet[curr] < quiet[ret]:
                    ret = curr
            res[node] = ret
            return ret
            
        starts = [i for i in range(n) if indeg[i] == 0]
        for start in starts:
            dfs(start)
        return res