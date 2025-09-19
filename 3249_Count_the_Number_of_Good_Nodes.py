class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        vis = set()
        res = 0
        def dfs(node):
            nonlocal vis, res
            vis.add(node)
            s = set()
            total = 0
            for neighbor in graph[node]:
                if neighbor not in vis:
                    val = dfs(neighbor)
                    s.add(val)
                    total += val
            if len(s) <= 1:
                res += 1
            return total + 1
        dfs(0)
        return res